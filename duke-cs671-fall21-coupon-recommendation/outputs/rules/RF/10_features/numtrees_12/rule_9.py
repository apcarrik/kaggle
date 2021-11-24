def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Education", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[3]<=3:
		# {"feature": "Coffeehouse", "instances": 81, "metric_value": 0.9867, "depth": 2}
		if obj[6]<=1.0:
			# {"feature": "Time", "instances": 43, "metric_value": 0.9103, "depth": 3}
			if obj[1]<=2:
				# {"feature": "Restaurant20to50", "instances": 33, "metric_value": 0.7455, "depth": 4}
				if obj[7]>-1.0:
					# {"feature": "Bar", "instances": 32, "metric_value": 0.6962, "depth": 5}
					if obj[5]<=1.0:
						# {"feature": "Coupon", "instances": 26, "metric_value": 0.5159, "depth": 6}
						if obj[2]>1:
							# {"feature": "Occupation", "instances": 18, "metric_value": 0.65, "depth": 7}
							if obj[4]<=6:
								# {"feature": "Passanger", "instances": 13, "metric_value": 0.7793, "depth": 8}
								if obj[0]>0:
									# {"feature": "Direction_same", "instances": 12, "metric_value": 0.8113, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 11, "metric_value": 0.8454, "depth": 10}
										if obj[9]<=2:
											return 'False'
										elif obj[9]>2:
											return 'False'
										else: return 'False'
									elif obj[8]>0:
										return 'False'
									else: return 'False'
								elif obj[0]<=0:
									return 'False'
								else: return 'False'
							elif obj[4]>6:
								return 'False'
							else: return 'False'
						elif obj[2]<=1:
							return 'False'
						else: return 'False'
					elif obj[5]>1.0:
						# {"feature": "Occupation", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[4]>6:
							# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[2]>0:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]>1:
									return 'True'
								elif obj[0]<=1:
									return 'False'
								else: return 'False'
							elif obj[2]<=0:
								return 'True'
							else: return 'True'
						elif obj[4]<=6:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[7]<=-1.0:
					return 'True'
				else: return 'True'
			elif obj[1]>2:
				# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[4]>3:
					# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 5}
					if obj[2]>1:
						# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[7]<=1.0:
							# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[0]>1:
								# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 9}
									if obj[8]<=0:
										# {"feature": "Distance", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[9]<=2:
											return 'True'
										else: return 'True'
									else: return 'True'
								else: return 'True'
							elif obj[0]<=1:
								return 'False'
							else: return 'False'
						elif obj[7]>1.0:
							return 'True'
						else: return 'True'
					elif obj[2]<=1:
						return 'False'
					else: return 'False'
				elif obj[4]<=3:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[6]>1.0:
			# {"feature": "Distance", "instances": 38, "metric_value": 0.992, "depth": 3}
			if obj[9]>1:
				# {"feature": "Occupation", "instances": 21, "metric_value": 0.9587, "depth": 4}
				if obj[4]>4:
					# {"feature": "Passanger", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[7]<=1.0:
							# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[2]<=1:
								# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[1]<=0:
									# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5]>2.0:
										return 'True'
									elif obj[5]<=2.0:
										return 'False'
									else: return 'False'
								elif obj[1]>0:
									return 'False'
								else: return 'False'
							elif obj[2]>1:
								return 'True'
							else: return 'True'
						elif obj[7]>1.0:
							return 'False'
						else: return 'False'
					elif obj[0]>1:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]>2:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0.0:
								return 'True'
							elif obj[5]>0.0:
								return 'False'
							else: return 'False'
						elif obj[1]<=2:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]<=4:
					# {"feature": "Time", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[1]<=3:
						# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[2]<=3:
								return 'False'
							elif obj[2]>3:
								# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[1]>3:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[9]<=1:
				# {"feature": "Time", "instances": 17, "metric_value": 0.7871, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Occupation", "instances": 15, "metric_value": 0.5665, "depth": 5}
					if obj[4]>2:
						return 'True'
					elif obj[4]<=2:
						# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[2]>1:
								# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=0.0:
									# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=1.0:
										# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[8]<=0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[5]>0.0:
									return 'False'
								else: return 'False'
							elif obj[2]<=1:
								return 'True'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[3]>3:
		return 'True'
	else: return 'True'
