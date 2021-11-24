def findDecision(obj): #obj[0]: Coupon, obj[1]: Education, obj[2]: Occupation, obj[3]: Restaurant20to50, obj[4]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[0]>0:
		# {"feature": "Education", "instances": 64, "metric_value": 0.9652, "depth": 2}
		if obj[1]<=2:
			# {"feature": "Distance", "instances": 53, "metric_value": 0.8836, "depth": 3}
			if obj[4]>1:
				# {"feature": "Occupation", "instances": 33, "metric_value": 0.9673, "depth": 4}
				if obj[2]<=21:
					# {"feature": "Restaurant20to50", "instances": 30, "metric_value": 0.9871, "depth": 5}
					if obj[3]<=2.0:
						return 'True'
					elif obj[3]>2.0:
						return 'True'
					else: return 'True'
				elif obj[2]>21:
					return 'True'
				else: return 'True'
			elif obj[4]<=1:
				# {"feature": "Restaurant20to50", "instances": 20, "metric_value": 0.6098, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Occupation", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[2]>2:
						return 'True'
					elif obj[2]<=2:
						return 'False'
					else: return 'False'
				elif obj[3]>1.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[1]>2:
			# {"feature": "Distance", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[4]>1:
				# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[2]>1:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[3]>0.0:
						return 'False'
					elif obj[3]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[2]<=1:
					return 'False'
				else: return 'False'
			elif obj[4]<=1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[0]<=0:
		# {"feature": "Occupation", "instances": 21, "metric_value": 0.7025, "depth": 2}
		if obj[2]>2:
			return 'False'
		elif obj[2]<=2:
			# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[3]<=1.0:
					# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[4]<=1:
						return 'False'
					elif obj[4]>1:
						return 'False'
					else: return 'False'
				elif obj[3]>1.0:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
