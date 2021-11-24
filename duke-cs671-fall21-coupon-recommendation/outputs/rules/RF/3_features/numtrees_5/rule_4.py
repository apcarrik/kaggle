def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 204, "metric_value": 0.9997, "depth": 1}
	if obj[0]>1:
		# {"feature": "Occupation", "instances": 141, "metric_value": 0.9648, "depth": 2}
		if obj[2]<=20.649728832182006:
			# {"feature": "Education", "instances": 132, "metric_value": 0.976, "depth": 3}
			if obj[1]<=4:
				return 'True'
			elif obj[1]>4:
				return 'True'
			else: return 'True'
		elif obj[2]>20.649728832182006:
			# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Education", "instances": 63, "metric_value": 0.8631, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Occupation", "instances": 49, "metric_value": 0.9313, "depth": 3}
			if obj[2]<=11:
				return 'False'
			elif obj[2]>11:
				return 'True'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.3712, "depth": 3}
			if obj[2]<=6:
				return 'False'
			elif obj[2]>6:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
