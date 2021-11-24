def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coupon", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[2]>0:
		# {"feature": "Coupon_validity", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[3]<=0:
			# {"feature": "Income", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[9]<=4:
				return 'True'
			elif obj[9]>4:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]>2:
					return 'False'
				elif obj[0]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[3]>0:
			# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=0:
		return 'False'
	else: return 'False'
