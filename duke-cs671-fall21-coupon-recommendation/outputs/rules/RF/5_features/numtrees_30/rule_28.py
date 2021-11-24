def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]>1:
		# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.9829, "depth": 2}
		if obj[3]>0.0:
			# {"feature": "Occupation", "instances": 24, "metric_value": 0.995, "depth": 3}
			if obj[2]<=7:
				# {"feature": "Distance", "instances": 20, "metric_value": 0.971, "depth": 4}
				if obj[4]>1:
					# {"feature": "Education", "instances": 15, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				elif obj[4]<=1:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[1]<=0:
						return 'True'
					elif obj[1]>0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[2]>7:
				# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[1]>2:
					# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]<=2:
						return 'True'
					else: return 'True'
				elif obj[1]<=2:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[3]<=0.0:
			return 'True'
		else: return 'True'
	elif obj[0]<=1:
		# {"feature": "Occupation", "instances": 8, "metric_value": 0.5436, "depth": 2}
		if obj[2]>1:
			return 'False'
		elif obj[2]<=1:
			return 'True'
		else: return 'True'
	else: return 'False'
