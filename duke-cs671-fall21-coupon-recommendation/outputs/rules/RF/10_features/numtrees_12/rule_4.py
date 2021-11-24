def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[4]<=19:
		# {"feature": "Time", "instances": 81, "metric_value": 0.999, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Coupon", "instances": 62, "metric_value": 0.9932, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Coffeehouse", "instances": 41, "metric_value": 0.9789, "depth": 4}
				if obj[6]<=3.0:
					# {"feature": "Direction_same", "instances": 38, "metric_value": 0.9495, "depth": 5}
					if obj[8]<=0:
						# {"feature": "Distance", "instances": 28, "metric_value": 0.8631, "depth": 6}
						if obj[9]>1:
							# {"feature": "Education", "instances": 19, "metric_value": 0.9495, "depth": 7}
							if obj[3]<=3:
								# {"feature": "Restaurant20to50", "instances": 18, "metric_value": 0.9183, "depth": 8}
								if obj[7]>0.0:
									# {"feature": "Passanger", "instances": 17, "metric_value": 0.874, "depth": 9}
									if obj[0]>0:
										# {"feature": "Bar", "instances": 14, "metric_value": 0.7496, "depth": 10}
										if obj[5]<=2.0:
											return 'True'
										elif obj[5]>2.0:
											return 'False'
										else: return 'False'
									elif obj[0]<=0:
										# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 10}
										if obj[5]<=1.0:
											return 'False'
										elif obj[5]>1.0:
											return 'True'
										else: return 'True'
									else: return 'False'
								elif obj[7]<=0.0:
									return 'False'
								else: return 'False'
							elif obj[3]>3:
								return 'False'
							else: return 'False'
						elif obj[9]<=1:
							# {"feature": "Education", "instances": 9, "metric_value": 0.5033, "depth": 7}
							if obj[3]<=1:
								return 'True'
							elif obj[3]>1:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=1.0:
									return 'True'
								elif obj[7]>1.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[8]>0:
						# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 6}
						if obj[9]<=1:
							# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[3]>2:
									# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]>1.0:
										return 'False'
									elif obj[7]<=1.0:
										return 'True'
									else: return 'True'
								elif obj[3]<=2:
									return 'False'
								else: return 'False'
							elif obj[5]>1.0:
								return 'True'
							else: return 'True'
						elif obj[9]>1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[6]>3.0:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				# {"feature": "Direction_same", "instances": 21, "metric_value": 0.7025, "depth": 4}
				if obj[8]<=0:
					# {"feature": "Coffeehouse", "instances": 18, "metric_value": 0.7642, "depth": 5}
					if obj[6]<=2.0:
						# {"feature": "Education", "instances": 16, "metric_value": 0.8113, "depth": 6}
						if obj[3]<=3:
							# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.7496, "depth": 7}
							if obj[7]<=1.0:
								# {"feature": "Distance", "instances": 12, "metric_value": 0.65, "depth": 8}
								if obj[9]>1:
									# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 9}
									if obj[0]<=2:
										# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 10}
										if obj[5]<=0.0:
											return 'False'
										elif obj[5]>0.0:
											return 'True'
										else: return 'True'
									elif obj[0]>2:
										# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[5]<=0.0:
											return 'False'
										else: return 'False'
									else: return 'False'
								elif obj[9]<=1:
									return 'False'
								else: return 'False'
							elif obj[7]>1.0:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=1:
									# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[5]<=0.0:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[9]<=1:
											return 'False'
										else: return 'False'
									else: return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[3]>3:
							# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[9]>1:
								return 'False'
							elif obj[9]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[6]>2.0:
						return 'False'
					else: return 'False'
				elif obj[8]>0:
					return 'False'
				else: return 'False'
			else: return 'False'
		elif obj[1]>3:
			# {"feature": "Education", "instances": 19, "metric_value": 0.8315, "depth": 3}
			if obj[3]<=0:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[2]>1:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[5]>0.0:
							# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[6]<=2.0:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]>0.0:
									return 'False'
								elif obj[7]<=0.0:
									return 'True'
								else: return 'True'
							elif obj[6]>2.0:
								return 'True'
							else: return 'True'
						elif obj[5]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				elif obj[2]<=1:
					return 'True'
				else: return 'True'
			elif obj[3]>0:
				# {"feature": "Distance", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[9]>1:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[0]>1:
						return 'False'
					elif obj[0]<=1:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[9]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[4]>19:
		return 'True'
	else: return 'True'
