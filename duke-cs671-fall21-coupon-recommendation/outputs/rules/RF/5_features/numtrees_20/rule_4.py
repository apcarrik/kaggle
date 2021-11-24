def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Occupation", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[2]>1:
		# {"feature": "Education", "instances": 43, "metric_value": 0.9902, "depth": 2}
		if obj[1]>0:
			# {"feature": "Distance", "instances": 29, "metric_value": 0.8936, "depth": 3}
			if obj[4]>1:
				# {"feature": "Coupon", "instances": 15, "metric_value": 0.5665, "depth": 4}
				if obj[0]>1:
					return 'False'
				elif obj[0]<=1:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[3]<=1.0:
						return 'False'
					elif obj[3]>1.0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]<=1:
				# {"feature": "Coupon", "instances": 14, "metric_value": 1.0, "depth": 4}
				if obj[0]>0:
					# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[3]>-1.0:
						return 'True'
					elif obj[3]<=-1.0:
						return 'True'
					else: return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Coupon", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[0]>0:
				# {"feature": "Distance", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[4]>1:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[3]<=1.0:
						return 'True'
					elif obj[3]>1.0:
						return 'False'
					else: return 'False'
				elif obj[4]<=1:
					return 'True'
				else: return 'True'
			elif obj[0]<=0:
				# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[4]<=2:
					return 'False'
				elif obj[4]>2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[2]<=1:
		return 'True'
	else: return 'True'
