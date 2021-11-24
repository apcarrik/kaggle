def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Coupon", "instances": 51, "metric_value": 0.9931, "depth": 1}
	if obj[1]>0:
		# {"feature": "Occupation", "instances": 48, "metric_value": 0.9799, "depth": 2}
		if obj[3]<=9:
			# {"feature": "Passanger", "instances": 32, "metric_value": 0.896, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Bar", "instances": 22, "metric_value": 0.976, "depth": 4}
				if obj[4]<=1.0:
					# {"feature": "Education", "instances": 16, "metric_value": 1.0, "depth": 5}
					if obj[2]<=0:
						# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 6}
						if obj[7]<=2:
							# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[5]>0.0:
								# {"feature": "Direction_same", "instances": 6, "metric_value": 0.65, "depth": 8}
								if obj[6]<=0:
									return 'True'
								elif obj[6]>0:
									return 'False'
								else: return 'False'
							elif obj[5]<=0.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[7]>2:
							return 'False'
						else: return 'False'
					elif obj[2]>0:
						# {"feature": "Distance", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[7]>1:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]<=1.0:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							elif obj[5]>1.0:
								return 'True'
							else: return 'True'
						elif obj[7]<=1:
							return 'False'
						else: return 'False'
					else: return 'False'
				elif obj[4]>1.0:
					# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 5}
					if obj[5]<=2.0:
						return 'True'
					elif obj[5]>2.0:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[2]<=3:
							return 'False'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[0]>1:
				# {"feature": "Distance", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[7]>1:
					return 'True'
				elif obj[7]<=1:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]<=0:
						return 'True'
					elif obj[2]>0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[3]>9:
			# {"feature": "Passanger", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[0]<=1:
				# {"feature": "Education", "instances": 13, "metric_value": 0.9957, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Bar", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[4]<=1.0:
						# {"feature": "Direction_same", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Distance", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[7]<=1:
								return 'True'
							elif obj[7]>1:
								# {"feature": "Restaurant20to50", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[5]<=1.0:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[6]>0:
							return 'False'
						else: return 'False'
					elif obj[4]>1.0:
						# {"feature": "Direction_same", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[6]<=0:
							return 'False'
						elif obj[6]>0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			elif obj[0]>1:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[1]<=0:
		return 'False'
	else: return 'False'
