def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 29, "metric_value": 0.9294, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 19, "metric_value": 0.998, "depth": 3}
			if obj[2]>2:
				# {"feature": "Distance", "instances": 17, "metric_value": 0.9975, "depth": 4}
				if obj[3]<=2:
					return 'False'
				elif obj[3]>2:
					return 'False'
				else: return 'False'
			elif obj[2]<=2:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Distance", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[3]>1:
				return 'True'
			elif obj[3]<=1:
				# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[2]<=2:
					return 'False'
				elif obj[2]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
