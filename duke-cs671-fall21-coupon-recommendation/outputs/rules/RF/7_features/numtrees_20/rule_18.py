def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Restaurant20to50, obj[5]: Direction_same, obj[6]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Education", "instances": 37, "metric_value": 0.9868, "depth": 2}
		if obj[2]>1:
			# {"feature": "Coupon", "instances": 21, "metric_value": 0.8631, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Distance", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Occupation", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[3]>2:
							# {"feature": "Direction_same", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								return 'False'
							else: return 'False'
						elif obj[3]<=2:
							return 'True'
						else: return 'True'
					elif obj[6]>2:
						return 'False'
					else: return 'False'
				elif obj[4]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[1]>2:
				return 'False'
			else: return 'False'
		elif obj[2]<=1:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[3]<=7:
				# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[4]>0.0:
					# {"feature": "Coupon", "instances": 11, "metric_value": 0.9457, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[5]<=0:
							return 'True'
						elif obj[5]>0:
							return 'False'
						else: return 'False'
					elif obj[1]>3:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[6]<=2:
							# {"feature": "Direction_same", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						elif obj[6]>2:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[4]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[3]>7:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Occupation", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[3]<=10:
			# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.6194, "depth": 3}
			if obj[4]>1.0:
				# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[1]>1:
					# {"feature": "Education", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[2]>0:
						# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[6]<=1:
							# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=0:
								return 'True'
							else: return 'True'
						elif obj[6]>1:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[2]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			elif obj[4]<=1.0:
				return 'True'
			else: return 'True'
		elif obj[3]>10:
			return 'False'
		else: return 'False'
	else: return 'True'
