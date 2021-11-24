def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 85, "metric_value": 0.9919, "depth": 1}
	if obj[1]>0:
		# {"feature": "Passanger", "instances": 73, "metric_value": 0.9506, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Bar", "instances": 57, "metric_value": 0.9891, "depth": 3}
			if obj[4]<=0.0:
				# {"feature": "Direction_same", "instances": 29, "metric_value": 0.8936, "depth": 4}
				if obj[6]<=0:
					# {"feature": "Occupation", "instances": 19, "metric_value": 0.9819, "depth": 5}
					if obj[3]>2:
						# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.7793, "depth": 6}
						if obj[5]>0.0:
							# {"feature": "Education", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[2]>0:
								# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[7]>2:
									return 'True'
								elif obj[7]<=2:
									return 'True'
								else: return 'True'
							elif obj[2]<=0:
								# {"feature": "Distance", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[7]<=1:
									return 'True'
								elif obj[7]>1:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[5]<=0.0:
							return 'True'
						else: return 'True'
					elif obj[3]<=2:
						# {"feature": "Education", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[2]<=0:
							return 'False'
						elif obj[2]>0:
							# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]<=2.0:
								# {"feature": "Distance", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]<=2:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[6]>0:
					# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 5}
					if obj[2]<=2:
						return 'True'
					elif obj[2]>2:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]<=1:
							# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]<=0.0:
								return 'True'
							elif obj[5]>0.0:
								return 'False'
							else: return 'False'
						elif obj[3]>1:
							return 'True'
						else: return 'True'
					else: return 'True'
				else: return 'True'
			elif obj[4]>0.0:
				# {"feature": "Education", "instances": 28, "metric_value": 0.9852, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.9612, "depth": 5}
					if obj[5]>0.0:
						# {"feature": "Distance", "instances": 24, "metric_value": 0.9799, "depth": 6}
						if obj[7]>1:
							# {"feature": "Occupation", "instances": 14, "metric_value": 1.0, "depth": 7}
							if obj[3]>1:
								# {"feature": "Direction_same", "instances": 13, "metric_value": 0.9957, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[3]<=1:
								return 'False'
							else: return 'False'
						elif obj[7]<=1:
							# {"feature": "Occupation", "instances": 10, "metric_value": 0.8813, "depth": 7}
							if obj[3]<=11:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 1.0, "depth": 8}
								if obj[6]>0:
									return 'False'
								elif obj[6]<=0:
									return 'True'
								else: return 'True'
							elif obj[3]>11:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[5]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[2]>3:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[0]>2:
			# {"feature": "Bar", "instances": 16, "metric_value": 0.5436, "depth": 3}
			if obj[4]>1.0:
				# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[5]>1.0:
					return 'True'
				elif obj[5]<=1.0:
					# {"feature": "Education", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]>6:
							# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[6]<=0:
								# {"feature": "Distance", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[7]<=2:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[3]<=6:
							return 'True'
						else: return 'True'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				else: return 'False'
			elif obj[4]<=1.0:
				return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[1]<=0:
		# {"feature": "Occupation", "instances": 12, "metric_value": 0.4138, "depth": 2}
		if obj[3]<=11:
			return 'False'
		elif obj[3]>11:
			# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[2]>0:
				return 'True'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
