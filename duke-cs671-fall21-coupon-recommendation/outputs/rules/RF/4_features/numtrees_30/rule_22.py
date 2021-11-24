def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Occupation", "instances": 29, "metric_value": 0.9784, "depth": 2}
		if obj[2]>2:
			# {"feature": "Coupon", "instances": 25, "metric_value": 0.9988, "depth": 3}
			if obj[0]>3:
				# {"feature": "Education", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[0]<=3:
				# {"feature": "Education", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]<=2:
			return 'True'
		else: return 'True'
	elif obj[3]>2:
		return 'False'
	else: return 'False'
