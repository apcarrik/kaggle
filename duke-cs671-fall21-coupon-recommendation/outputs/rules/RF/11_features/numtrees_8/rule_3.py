def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coffeehouse", "instances": 127, "metric_value": 0.9566, "depth": 1}
	if obj[7]>0.0:
		# {"feature": "Education", "instances": 94, "metric_value": 0.8651, "depth": 2}
		if obj[4]<=1:
			# {"feature": "Passanger", "instances": 48, "metric_value": 0.6962, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Coupon", "instances": 33, "metric_value": 0.8454, "depth": 4}
				if obj[2]>1:
					# {"feature": "Age", "instances": 21, "metric_value": 0.5917, "depth": 5}
					if obj[3]>1:
						# {"feature": "Occupation", "instances": 12, "metric_value": 0.8113, "depth": 6}
						if obj[5]<=18:
							# {"feature": "Time", "instances": 11, "metric_value": 0.684, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[9]<=0:
									# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 9}
									if obj[6]<=0.0:
										# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 10}
										if obj[10]<=1:
											# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 11}
											if obj[8]<=1.0:
												return 'False'
											else: return 'False'
										elif obj[10]>1:
											return 'True'
										else: return 'True'
									elif obj[6]>0.0:
										return 'True'
									else: return 'True'
								elif obj[9]>0:
									return 'True'
								else: return 'True'
							elif obj[1]>1:
								return 'True'
							else: return 'True'
						elif obj[5]>18:
							return 'False'
						else: return 'False'
					elif obj[3]<=1:
						return 'True'
					else: return 'True'
				elif obj[2]<=1:
					# {"feature": "Time", "instances": 12, "metric_value": 1.0, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Age", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[3]<=1:
							# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[5]>2:
								return 'True'
							elif obj[5]<=2:
								# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[10]<=1:
									return 'False'
								elif obj[10]>1:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[3]>1:
							return 'False'
						else: return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		elif obj[4]>1:
			# {"feature": "Age", "instances": 46, "metric_value": 0.9656, "depth": 3}
			if obj[3]<=3:
				# {"feature": "Occupation", "instances": 23, "metric_value": 0.8281, "depth": 4}
				if obj[5]<=8:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.3912, "depth": 5}
					if obj[2]>2:
						return 'True'
					elif obj[2]<=2:
						# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[10]<=2:
							return 'True'
						elif obj[10]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[5]>8:
					# {"feature": "Coupon", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[2]>1:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[0]>1:
							return 'False'
						elif obj[0]<=1:
							# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[10]<=2:
								return 'True'
							elif obj[10]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[2]<=1:
						return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[3]>3:
				# {"feature": "Direction_same", "instances": 23, "metric_value": 0.9986, "depth": 4}
				if obj[9]<=0:
					# {"feature": "Passanger", "instances": 19, "metric_value": 0.9819, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Coupon", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[2]>0:
							# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[1]>1:
								# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[10]>1:
									return 'True'
								elif obj[10]<=1:
									return 'False'
								else: return 'False'
							elif obj[1]<=1:
								return 'False'
							else: return 'False'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						# {"feature": "Time", "instances": 9, "metric_value": 0.7642, "depth": 6}
						if obj[1]<=2:
							# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 7}
							if obj[2]>1:
								return 'True'
							elif obj[2]<=1:
								return 'False'
							else: return 'False'
						elif obj[1]>2:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[9]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[7]<=0.0:
		# {"feature": "Distance", "instances": 33, "metric_value": 0.9457, "depth": 2}
		if obj[10]>1:
			# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 3}
			if obj[5]>1:
				# {"feature": "Time", "instances": 20, "metric_value": 0.9928, "depth": 4}
				if obj[1]>1:
					# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.971, "depth": 5}
					if obj[8]<=1.0:
						# {"feature": "Passanger", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[0]<=2:
							return 'False'
						elif obj[0]>2:
							# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[3]>1:
								# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[2]>1:
									# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[4]<=0:
										# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[6]<=0.0:
											# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[2]<=1:
									return 'False'
								else: return 'False'
							elif obj[3]<=1:
								return 'True'
							else: return 'True'
						else: return 'True'
					elif obj[8]>1.0:
						return 'True'
					else: return 'True'
				elif obj[1]<=1:
					return 'True'
				else: return 'True'
			elif obj[5]<=1:
				return 'False'
			else: return 'False'
		elif obj[10]<=1:
			# {"feature": "Time", "instances": 10, "metric_value": 0.469, "depth": 3}
			if obj[1]<=1:
				return 'False'
			elif obj[1]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
