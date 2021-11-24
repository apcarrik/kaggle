def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.987, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 109, "metric_value": 0.9617, "depth": 2}
		if obj[2]<=19.263429492229875:
			# {"feature": "Education", "instances": 103, "metric_value": 0.9498, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'True'
			else: return 'True'
		elif obj[2]>19.263429492229875:
			# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[1]<=2:
				return 'False'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=0:
		# {"feature": "Education", "instances": 18, "metric_value": 0.8524, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[2]>1:
				return 'False'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		elif obj[1]<=0:
			# {"feature": "Occupation", "instances": 8, "metric_value": 1.0, "depth": 3}
			if obj[2]>2:
				return 'True'
			elif obj[2]<=2:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'False'
