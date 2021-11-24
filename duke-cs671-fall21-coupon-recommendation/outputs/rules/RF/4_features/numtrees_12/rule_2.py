def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[2]>0:
		# {"feature": "Distance", "instances": 81, "metric_value": 0.9972, "depth": 2}
		if obj[3]<=2:
			# {"feature": "Coupon", "instances": 69, "metric_value": 0.9998, "depth": 3}
			if obj[0]>2:
				# {"feature": "Education", "instances": 42, "metric_value": 0.9852, "depth": 4}
				if obj[1]<=4:
					return 'False'
				elif obj[1]>4:
					return 'True'
				else: return 'True'
			elif obj[0]<=2:
				# {"feature": "Education", "instances": 27, "metric_value": 0.951, "depth": 4}
				if obj[1]>1:
					return 'False'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[3]>2:
			# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[0]>0:
					return 'False'
				elif obj[0]<=0:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[2]<=0:
		return 'True'
	else: return 'True'
