def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Coffeehouse", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[7]>1.0:
		# {"feature": "Passanger", "instances": 43, "metric_value": 0.933, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Direction_same", "instances": 27, "metric_value": 0.999, "depth": 3}
			if obj[9]<=0:
				# {"feature": "Time", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[1]>0:
					# {"feature": "Age", "instances": 14, "metric_value": 0.8631, "depth": 5}
					if obj[3]>0:
						# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[8]<=2.0:
							# {"feature": "Coupon", "instances": 12, "metric_value": 0.65, "depth": 7}
							if obj[2]>2:
								return 'False'
							elif obj[2]<=2:
								# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 8}
								if obj[6]>-1.0:
									# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 9}
									if obj[5]>1:
										return 'False'
									elif obj[5]<=1:
										# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 10}
										if obj[10]>1:
											return 'True'
										elif obj[10]<=1:
											return 'False'
										else: return 'False'
									else: return 'True'
								elif obj[6]<=-1.0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[8]>2.0:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						return 'True'
					else: return 'True'
				elif obj[1]<=0:
					return 'True'
				else: return 'True'
			elif obj[9]>0:
				# {"feature": "Bar", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[6]<=1.0:
					return 'True'
				elif obj[6]>1.0:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[5]>6:
						# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[8]<=1.0:
							return 'True'
						elif obj[8]>1.0:
							return 'False'
						else: return 'False'
					elif obj[5]<=6:
						return 'False'
					else: return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.5436, "depth": 3}
			if obj[5]<=4:
				return 'True'
			elif obj[5]>4:
				# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[1]>2:
						return 'True'
					elif obj[1]<=2:
						# {"feature": "Bar", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]>1.0:
							return 'True'
						elif obj[6]<=1.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[4]>2:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'True'
	elif obj[7]<=1.0:
		# {"feature": "Occupation", "instances": 42, "metric_value": 0.9403, "depth": 2}
		if obj[5]>4:
			# {"feature": "Coupon", "instances": 28, "metric_value": 0.7496, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Bar", "instances": 16, "metric_value": 0.9544, "depth": 4}
				if obj[6]>0.0:
					# {"feature": "Time", "instances": 12, "metric_value": 1.0, "depth": 5}
					if obj[1]<=2:
						# {"feature": "Education", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[4]<=2:
							# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 7}
							if obj[0]>0:
								# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 8}
								if obj[10]>2:
									# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[8]<=1.0:
										return 'True'
									elif obj[8]>1.0:
										return 'False'
									else: return 'False'
								elif obj[10]<=2:
									return 'False'
								else: return 'False'
							elif obj[0]<=0:
								return 'True'
							else: return 'True'
						elif obj[4]>2:
							return 'False'
						else: return 'False'
					elif obj[1]>2:
						# {"feature": "Passanger", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[0]<=1:
							return 'True'
						elif obj[0]>1:
							# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]>0:
								return 'False'
							elif obj[3]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'True'
				elif obj[6]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		elif obj[5]<=4:
			# {"feature": "Restaurant20to50", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[8]<=1.0:
				# {"feature": "Time", "instances": 9, "metric_value": 0.9911, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]>3:
						return 'False'
					elif obj[2]<=3:
						# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=1:
							return 'True'
						elif obj[3]>1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]>1:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[8]>1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'False'
