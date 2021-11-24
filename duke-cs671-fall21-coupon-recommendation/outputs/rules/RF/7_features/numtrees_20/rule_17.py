def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Restaurant20to50", "instances": 51, "metric_value": 0.9662, "depth": 1}
	if obj[4]<=2.0:
		# {"feature": "Passanger", "instances": 46, "metric_value": 0.9877, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Education", "instances": 28, "metric_value": 0.9852, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Distance", "instances": 25, "metric_value": 0.9427, "depth": 4}
				if obj[6]>1:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[1]>1:
						# {"feature": "Occupation", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[3]>1:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[3]<=1:
							return 'False'
						else: return 'False'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				elif obj[6]<=1:
					# {"feature": "Coupon", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[1]>0:
						# {"feature": "Occupation", "instances": 11, "metric_value": 0.9457, "depth": 6}
						if obj[3]>2:
							# {"feature": "Direction_same", "instances": 10, "metric_value": 0.971, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[3]<=2:
							return 'True'
						else: return 'True'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[2]>3:
				return 'True'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Coupon", "instances": 18, "metric_value": 0.7642, "depth": 3}
			if obj[1]>2:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 4}
				if obj[3]<=11:
					# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[6]>1:
							# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]<=1:
							return 'True'
						else: return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				elif obj[3]>11:
					return 'True'
				else: return 'True'
			elif obj[1]<=2:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]>2.0:
		return 'True'
	else: return 'True'
