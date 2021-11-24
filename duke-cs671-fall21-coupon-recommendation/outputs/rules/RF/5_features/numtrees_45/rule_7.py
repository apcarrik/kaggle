def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[2]<=6:
		# {"feature": "Coupon", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[0]>0:
			# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 3}
			if obj[1]<=1:
				return 'True'
			elif obj[1]>1:
				# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]>1.0:
					return 'True'
				elif obj[3]<=1.0:
					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[0]<=0:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[2]>6:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 2}
		if obj[0]>2:
			# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[1]>0:
				return 'True'
			elif obj[1]<=0:
				return 'False'
			else: return 'False'
		elif obj[0]<=2:
			return 'False'
		else: return 'False'
	else: return 'False'
