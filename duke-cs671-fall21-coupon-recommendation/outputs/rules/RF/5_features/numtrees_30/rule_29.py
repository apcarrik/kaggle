def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Distance", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[4]>1:
		# {"feature": "Coupon", "instances": 18, "metric_value": 0.9183, "depth": 2}
		if obj[0]>1:
			# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 1.0, "depth": 3}
			if obj[3]<=1.0:
				# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[1]>0:
					# {"feature": "Occupation", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[2]>7:
						return 'True'
					elif obj[2]<=7:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'False'
				else: return 'False'
			elif obj[3]>1.0:
				# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[1]<=2:
					return 'False'
				elif obj[1]>2:
					# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[2]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]<=1:
			return 'False'
		else: return 'False'
	elif obj[4]<=1:
		# {"feature": "Occupation", "instances": 16, "metric_value": 0.896, "depth": 2}
		if obj[2]<=8:
			# {"feature": "Coupon", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[0]>0:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[3]>-1.0:
					# {"feature": "Education", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[1]<=2:
						return 'True'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				elif obj[3]<=-1.0:
					return 'False'
				else: return 'False'
			elif obj[0]<=0:
				return 'False'
			else: return 'False'
		elif obj[2]>8:
			return 'True'
		else: return 'True'
	else: return 'True'
