def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 30, "metric_value": 0.9968, "depth": 2}
		if obj[2]>2:
			# {"feature": "Education", "instances": 24, "metric_value": 0.995, "depth": 3}
			if obj[1]>1:
				# {"feature": "Distance", "instances": 17, "metric_value": 0.9367, "depth": 4}
				if obj[4]>1:
					# {"feature": "Restaurant20to50", "instances": 16, "metric_value": 0.9544, "depth": 5}
					if obj[3]<=1.0:
						return 'False'
					elif obj[3]>1.0:
						return 'False'
					else: return 'False'
				elif obj[4]<=1:
					return 'False'
				else: return 'False'
			elif obj[1]<=1:
				# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[3]<=2.0:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=2:
						return 'True'
					elif obj[4]>2:
						return 'True'
					else: return 'True'
				elif obj[3]>2.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]<=2:
			# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[3]<=1.0:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]>1:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			elif obj[3]>1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=0:
		return 'False'
	else: return 'False'
