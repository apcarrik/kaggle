def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[9]<=6:
		# {"feature": "Weather", "instances": 20, "metric_value": 0.6098, "depth": 2}
		if obj[1]<=0:
			# {"feature": "Restaurant20to50", "instances": 17, "metric_value": 0.3228, "depth": 3}
			if obj[13]<=3.0:
				return 'True'
			elif obj[13]>3.0:
				return 'False'
			else: return 'False'
		elif obj[1]>0:
			# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[0]<=0:
				return 'False'
			elif obj[0]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[9]>6:
		# {"feature": "Income", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[10]<=3:
			return 'False'
		elif obj[10]>3:
			# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[6]<=2:
				# {"feature": "Coupon_validity", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[4]>0:
					return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			elif obj[6]>2:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
