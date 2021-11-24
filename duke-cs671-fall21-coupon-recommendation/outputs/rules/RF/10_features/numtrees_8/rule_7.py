def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9235, "depth": 1}
	if obj[2]>0:
		# {"feature": "Passanger", "instances": 110, "metric_value": 0.8579, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Education", "instances": 76, "metric_value": 0.9268, "depth": 3}
			if obj[3]<=2:
				# {"feature": "Occupation", "instances": 60, "metric_value": 0.9604, "depth": 4}
				if obj[4]<=13:
					# {"feature": "Coffeehouse", "instances": 53, "metric_value": 0.9052, "depth": 5}
					if obj[6]<=3.0:
						# {"feature": "Bar", "instances": 51, "metric_value": 0.874, "depth": 6}
						if obj[5]<=3.0:
							# {"feature": "Time", "instances": 50, "metric_value": 0.8555, "depth": 7}
							if obj[1]<=3:
								# {"feature": "Direction_same", "instances": 42, "metric_value": 0.7919, "depth": 8}
								if obj[8]<=0:
									# {"feature": "Restaurant20to50", "instances": 29, "metric_value": 0.8498, "depth": 9}
									if obj[7]>0.0:
										# {"feature": "Distance", "instances": 26, "metric_value": 0.8905, "depth": 10}
										if obj[9]<=2:
											return 'True'
										elif obj[9]>2:
											return 'True'
										else: return 'True'
									elif obj[7]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[8]>0:
									# {"feature": "Distance", "instances": 13, "metric_value": 0.6194, "depth": 9}
									if obj[9]<=1:
										# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 10}
										if obj[7]>0.0:
											return 'True'
										elif obj[7]<=0.0:
											return 'True'
										else: return 'True'
									elif obj[9]>1:
										return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[1]>3:
								# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 1.0, "depth": 8}
								if obj[7]<=2.0:
									# {"feature": "Distance", "instances": 7, "metric_value": 0.9852, "depth": 9}
									if obj[9]<=1:
										# {"feature": "Direction_same", "instances": 5, "metric_value": 0.971, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									elif obj[9]>1:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									else: return 'True'
								elif obj[7]>2.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[5]>3.0:
							return 'False'
						else: return 'False'
					elif obj[6]>3.0:
						return 'False'
					else: return 'False'
				elif obj[4]>13:
					# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[1]<=3:
						return 'False'
					elif obj[1]>3:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[3]>2:
				# {"feature": "Coffeehouse", "instances": 16, "metric_value": 0.6962, "depth": 4}
				if obj[6]>1.0:
					# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[4]>2:
							# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=1:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[7]<=2.0:
									return 'True'
								elif obj[7]>2.0:
									# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[8]<=0:
										return 'False'
									elif obj[8]>0:
										return 'True'
									else: return 'True'
								else: return 'False'
							elif obj[1]>1:
								return 'False'
							else: return 'False'
						elif obj[4]<=2:
							return 'True'
						else: return 'True'
					elif obj[5]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[6]<=1.0:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Bar", "instances": 34, "metric_value": 0.6024, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Restaurant20to50", "instances": 25, "metric_value": 0.7219, "depth": 4}
				if obj[7]<=2.0:
					# {"feature": "Time", "instances": 24, "metric_value": 0.65, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Occupation", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[4]<=6:
							# {"feature": "Education", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[3]>0:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[9]>1:
									# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[6]>0.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'True'
										else: return 'True'
									elif obj[6]<=0.0:
										return 'True'
									else: return 'True'
								elif obj[9]<=1:
									return 'False'
								else: return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						elif obj[4]>6:
							# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[6]>0.0:
								return 'True'
							elif obj[6]<=0.0:
								# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[3]<=0:
									return 'False'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						else: return 'True'
					elif obj[1]>2:
						return 'True'
					else: return 'True'
				elif obj[7]>2.0:
					return 'False'
				else: return 'False'
			elif obj[5]>1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[2]<=0:
		# {"feature": "Time", "instances": 17, "metric_value": 0.874, "depth": 2}
		if obj[1]>0:
			# {"feature": "Occupation", "instances": 11, "metric_value": 0.994, "depth": 3}
			if obj[4]<=9:
				# {"feature": "Bar", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[5]<=2.0:
					# {"feature": "Distance", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[9]>1:
						# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[3]>0:
							return 'False'
						elif obj[3]<=0:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Coffeehouse", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]>3.0:
									return 'False'
								elif obj[6]<=3.0:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[9]<=1:
						return 'True'
					else: return 'True'
				elif obj[5]>2.0:
					return 'True'
				else: return 'True'
			elif obj[4]>9:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	else: return 'False'
