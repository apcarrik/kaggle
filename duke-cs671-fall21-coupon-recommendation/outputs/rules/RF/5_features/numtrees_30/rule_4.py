def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 0.9975, "depth": 1}
	if obj[0]>0:
		# {"feature": "Occupation", "instances": 24, "metric_value": 0.8709, "depth": 2}
		if obj[2]<=10:
			# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[3]<=1.0:
				# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[1]>1:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[4]>1:
						return 'True'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				elif obj[1]<=1:
					# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[4]>1:
						return 'False'
					elif obj[4]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]>1.0:
				# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 4}
				if obj[4]<=1:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[1]>1:
						return 'True'
					elif obj[1]<=1:
						return 'True'
					else: return 'True'
				elif obj[4]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[2]>10:
			# {"feature": "Distance", "instances": 9, "metric_value": 0.5033, "depth": 3}
			if obj[4]<=1:
				return 'True'
			elif obj[4]>1:
				# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[3]>1.0:
					return 'True'
				elif obj[3]<=1.0:
					# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[1]<=2:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[0]<=0:
		# {"feature": "Occupation", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[2]<=6:
			return 'False'
		elif obj[2]>6:
			return 'True'
		else: return 'True'
	else: return 'False'
