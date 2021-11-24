def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coffeehouse", "instances": 85, "metric_value": 0.9774, "depth": 1}
	if obj[7]<=1.0:
		# {"feature": "Occupation", "instances": 44, "metric_value": 0.994, "depth": 2}
		if obj[5]<=14:
			# {"feature": "Coupon", "instances": 36, "metric_value": 0.9978, "depth": 3}
			if obj[2]>0:
				# {"feature": "Education", "instances": 28, "metric_value": 0.9666, "depth": 4}
				if obj[4]<=1:
					# {"feature": "Age", "instances": 18, "metric_value": 1.0, "depth": 5}
					if obj[3]<=4:
						# {"feature": "Time", "instances": 16, "metric_value": 0.9887, "depth": 6}
						if obj[1]>0:
							# {"feature": "Bar", "instances": 11, "metric_value": 0.994, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Distance", "instances": 10, "metric_value": 0.971, "depth": 8}
								if obj[10]>1:
									# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 9}
									if obj[0]>0:
										# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.9852, "depth": 10}
										if obj[8]>-1.0:
											# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 11}
											if obj[9]<=0:
												return 'True'
											else: return 'True'
										elif obj[8]<=-1.0:
											return 'True'
										else: return 'True'
									elif obj[0]<=0:
										return 'False'
									else: return 'False'
								elif obj[10]<=1:
									return 'True'
								else: return 'True'
							elif obj[6]>1.0:
								return 'False'
							else: return 'False'
						elif obj[1]<=0:
							# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[6]<=1.0:
								return 'False'
							elif obj[6]>1.0:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[3]>4:
						return 'True'
					else: return 'True'
				elif obj[4]>1:
					# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[8]>1.0:
						return 'True'
					elif obj[8]<=1.0:
						# {"feature": "Passanger", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[1]<=1:
								return 'True'
							elif obj[1]>1:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			elif obj[2]<=0:
				# {"feature": "Time", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[4]>0:
						# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[6]<=0.0:
							return 'False'
						elif obj[6]>0.0:
							return 'True'
						else: return 'True'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]>14:
			# {"feature": "Time", "instances": 8, "metric_value": 0.5436, "depth": 3}
			if obj[1]<=3:
				return 'False'
			elif obj[1]>3:
				# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[7]>1.0:
		# {"feature": "Occupation", "instances": 41, "metric_value": 0.839, "depth": 2}
		if obj[5]>1:
			# {"feature": "Coupon", "instances": 34, "metric_value": 0.9082, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Education", "instances": 23, "metric_value": 0.7554, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Time", "instances": 17, "metric_value": 0.874, "depth": 5}
					if obj[1]>0:
						# {"feature": "Age", "instances": 13, "metric_value": 0.9612, "depth": 6}
						if obj[3]>1:
							# {"feature": "Bar", "instances": 7, "metric_value": 0.9852, "depth": 7}
							if obj[6]<=1.0:
								# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[8]<=1.0:
									# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[0]>1:
										return 'False'
									elif obj[0]<=1:
										return 'True'
									else: return 'True'
								elif obj[8]>1.0:
									return 'True'
								else: return 'True'
							elif obj[6]>1.0:
								return 'False'
							else: return 'False'
						elif obj[3]<=1:
							# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[6]<=2.0:
								return 'True'
							elif obj[6]>2.0:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[8]>2.0:
									return 'True'
								elif obj[8]<=2.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						else: return 'True'
					elif obj[1]<=0:
						return 'True'
					else: return 'True'
				elif obj[4]>2:
					return 'True'
				else: return 'True'
			elif obj[2]>3:
				# {"feature": "Distance", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[10]<=1:
					# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[3]>0:
						return 'False'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[10]>1:
					# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[4]<=0:
						return 'True'
					elif obj[4]>0:
						# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]>1:
							return 'True'
						elif obj[3]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[5]<=1:
			return 'True'
		else: return 'True'
	else: return 'True'
