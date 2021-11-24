def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9309, "depth": 1}
	if obj[1]>0:
		# {"feature": "Restaurant20to50", "instances": 110, "metric_value": 0.8699, "depth": 2}
		if obj[5]>-1.0:
			# {"feature": "Distance", "instances": 108, "metric_value": 0.8524, "depth": 3}
			if obj[7]>1:
				# {"feature": "Occupation", "instances": 61, "metric_value": 0.9432, "depth": 4}
				if obj[3]<=14:
					# {"feature": "Bar", "instances": 57, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Education", "instances": 37, "metric_value": 0.8419, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Passanger", "instances": 35, "metric_value": 0.8631, "depth": 7}
							if obj[0]>1:
								# {"feature": "Direction_same", "instances": 19, "metric_value": 0.8997, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[0]<=1:
								# {"feature": "Direction_same", "instances": 16, "metric_value": 0.8113, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					elif obj[4]>1.0:
						# {"feature": "Direction_same", "instances": 20, "metric_value": 0.9928, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Education", "instances": 19, "metric_value": 0.9819, "depth": 7}
							if obj[2]>0:
								# {"feature": "Passanger", "instances": 14, "metric_value": 0.9403, "depth": 8}
								if obj[0]<=2:
									return 'True'
								elif obj[0]>2:
									return 'True'
								else: return 'True'
							elif obj[2]<=0:
								# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[0]>1:
									return 'True'
								elif obj[0]<=1:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[6]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[3]>14:
					# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[7]<=1:
				# {"feature": "Occupation", "instances": 47, "metric_value": 0.6582, "depth": 4}
				if obj[3]>1:
					# {"feature": "Direction_same", "instances": 38, "metric_value": 0.7425, "depth": 5}
					if obj[6]<=0:
						# {"feature": "Education", "instances": 33, "metric_value": 0.799, "depth": 6}
						if obj[2]>1:
							# {"feature": "Bar", "instances": 18, "metric_value": 0.9183, "depth": 7}
							if obj[4]<=1.0:
								# {"feature": "Passanger", "instances": 14, "metric_value": 0.7496, "depth": 8}
								if obj[0]<=2:
									return 'True'
								elif obj[0]>2:
									return 'True'
								else: return 'True'
							elif obj[4]>1.0:
								# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[0]>0:
									return 'False'
								elif obj[0]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[2]<=1:
							# {"feature": "Bar", "instances": 15, "metric_value": 0.5665, "depth": 7}
							if obj[4]<=0.0:
								# {"feature": "Passanger", "instances": 8, "metric_value": 0.8113, "depth": 8}
								if obj[0]>0:
									return 'True'
								elif obj[0]<=0:
									return 'True'
								else: return 'True'
							elif obj[4]>0.0:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[6]>0:
						return 'True'
					else: return 'True'
				elif obj[3]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[5]<=-1.0:
			return 'False'
		else: return 'False'
	elif obj[1]<=0:
		# {"feature": "Passanger", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.5917, "depth": 3}
			if obj[3]>0:
				# {"feature": "Bar", "instances": 13, "metric_value": 0.3912, "depth": 4}
				if obj[4]<=1.0:
					return 'False'
				elif obj[4]>1.0:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[5]<=1.0:
							return 'True'
						elif obj[5]>1.0:
							return 'False'
						else: return 'False'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[3]<=0:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
