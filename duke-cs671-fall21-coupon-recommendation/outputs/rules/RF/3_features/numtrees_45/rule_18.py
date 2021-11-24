def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[2]<=7:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.8631, "depth": 2}
		if obj[0]>1:
			# {"feature": "Education", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		elif obj[0]<=1:
			# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=0:
				return 'False'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[2]>7:
		# {"feature": "Coupon", "instances": 9, "metric_value": 0.9183, "depth": 2}
		if obj[0]>3:
			# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[1]<=0:
				return 'False'
			elif obj[1]>0:
				return 'False'
			else: return 'False'
		elif obj[0]<=3:
			# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[1]>0:
				return 'False'
			elif obj[1]<=0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
