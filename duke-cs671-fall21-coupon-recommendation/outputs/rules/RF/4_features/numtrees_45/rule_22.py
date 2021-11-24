def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[1]>0:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.9852, "depth": 2}
		if obj[2]<=12:
			# {"feature": "Coupon", "instances": 12, "metric_value": 1.0, "depth": 3}
			if obj[0]>2:
				# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=2:
					return 'True'
				elif obj[3]>2:
					return 'True'
				else: return 'True'
			elif obj[0]<=2:
				# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[3]>1:
					return 'False'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]>12:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		return 'True'
	else: return 'True'
