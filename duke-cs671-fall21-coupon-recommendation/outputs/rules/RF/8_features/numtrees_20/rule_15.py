def findDecision(obj): #obj[0]: Passanger, obj[1]: Coupon, obj[2]: Education, obj[3]: Occupation, obj[4]: Bar, obj[5]: Restaurant20to50, obj[6]: Direction_same, obj[7]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9975, "depth": 1}
	if obj[7]>1:
		# {"feature": "Coupon", "instances": 32, "metric_value": 0.9544, "depth": 2}
		if obj[1]>1:
			# {"feature": "Restaurant20to50", "instances": 21, "metric_value": 0.9984, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Occupation", "instances": 20, "metric_value": 0.9928, "depth": 4}
				if obj[3]>1:
					# {"feature": "Bar", "instances": 14, "metric_value": 0.9403, "depth": 5}
					if obj[4]>0.0:
						# {"feature": "Direction_same", "instances": 11, "metric_value": 0.994, "depth": 6}
						if obj[6]<=0:
							# {"feature": "Education", "instances": 9, "metric_value": 0.9911, "depth": 7}
							if obj[2]<=3:
								# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 8}
								if obj[0]<=1:
									return 'False'
								elif obj[0]>1:
									return 'True'
								else: return 'True'
							elif obj[2]>3:
								return 'False'
							else: return 'False'
						elif obj[6]>0:
							return 'False'
						else: return 'False'
					elif obj[4]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[3]<=1:
					# {"feature": "Passanger", "instances": 6, "metric_value": 0.9183, "depth": 5}
					if obj[0]<=2:
						# {"feature": "Education", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[2]>0:
							return 'True'
						elif obj[2]<=0:
							# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[4]<=0.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[0]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]>2.0:
				return 'True'
			else: return 'True'
		elif obj[1]<=1:
			# {"feature": "Passanger", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[3]<=5:
					return 'False'
				elif obj[3]>5:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[7]<=1:
		# {"feature": "Occupation", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[3]<=10:
			# {"feature": "Restaurant20to50", "instances": 15, "metric_value": 0.9968, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Passanger", "instances": 14, "metric_value": 0.9852, "depth": 4}
				if obj[0]<=1:
					# {"feature": "Coupon", "instances": 11, "metric_value": 0.994, "depth": 5}
					if obj[1]>1:
						# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[2]<=2:
							# {"feature": "Bar", "instances": 6, "metric_value": 0.65, "depth": 7}
							if obj[4]>0.0:
								return 'False'
							elif obj[4]<=0.0:
								# {"feature": "Direction_same", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[6]<=0:
									return 'False'
								elif obj[6]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					elif obj[1]<=1:
						# {"feature": "Bar", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]>0.0:
							return 'True'
						elif obj[4]<=0.0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[0]>1:
					return 'True'
				else: return 'True'
			elif obj[5]>2.0:
				return 'False'
			else: return 'False'
		elif obj[3]>10:
			return 'True'
		else: return 'True'
	else: return 'True'
