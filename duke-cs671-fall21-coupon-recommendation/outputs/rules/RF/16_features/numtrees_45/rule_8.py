def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[9]>5:
		# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9183, "depth": 2}
		if obj[13]<=1.0:
			# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[2]>0:
				return 'False'
			elif obj[2]<=0:
				# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[4]>0:
					return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[13]>1.0:
			# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[0]>1:
				return 'True'
			elif obj[0]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[9]<=5:
		# {"feature": "Coupon", "instances": 11, "metric_value": 0.684, "depth": 2}
		if obj[3]>0:
			return 'True'
		elif obj[3]<=0:
			# {"feature": "Weather", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[1]<=0:
				return 'True'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'True'
