def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 85, "metric_value": 0.9951, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Distance", "instances": 65, "metric_value": 0.9916, "depth": 2}
		if obj[12]>1:
			# {"feature": "Occupation", "instances": 40, "metric_value": 0.9544, "depth": 3}
			if obj[7]<=11:
				# {"feature": "Age", "instances": 34, "metric_value": 0.99, "depth": 4}
				if obj[4]<=4:
					# {"feature": "Gender", "instances": 27, "metric_value": 0.951, "depth": 5}
					if obj[3]>0:
						# {"feature": "Direction_same", "instances": 14, "metric_value": 0.7496, "depth": 6}
						if obj[11]<=0:
							# {"feature": "Restaurant20to50", "instances": 13, "metric_value": 0.6194, "depth": 7}
							if obj[10]<=1.0:
								# {"feature": "Education", "instances": 7, "metric_value": 0.8631, "depth": 8}
								if obj[6]<=2:
									# {"feature": "Coffeehouse", "instances": 4, "metric_value": 1.0, "depth": 9}
									if obj[9]>1.0:
										return 'True'
									elif obj[9]<=1.0:
										return 'False'
									else: return 'False'
								elif obj[6]>2:
									return 'False'
								else: return 'False'
							elif obj[10]>1.0:
								return 'False'
							else: return 'False'
						elif obj[11]>0:
							return 'True'
						else: return 'True'
					elif obj[3]<=0:
						# {"feature": "Coupon", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[2]<=3:
							# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 7}
							if obj[6]>1:
								return 'False'
							elif obj[6]<=1:
								# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 8}
								if obj[1]>0:
									# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 9}
									if obj[5]>0:
										return 'True'
									elif obj[5]<=0:
										return 'False'
									else: return 'False'
								elif obj[1]<=0:
									return 'False'
								else: return 'False'
							else: return 'False'
						elif obj[2]>3:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>4:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[10]>0.0:
						return 'True'
					elif obj[10]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]>11:
				return 'False'
			else: return 'False'
		elif obj[12]<=1:
			# {"feature": "Age", "instances": 25, "metric_value": 0.9896, "depth": 3}
			if obj[4]>1:
				# {"feature": "Direction_same", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[11]<=0:
					# {"feature": "Gender", "instances": 10, "metric_value": 0.7219, "depth": 5}
					if obj[3]>0:
						# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[2]>1:
							# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[1]<=2:
								return 'True'
							elif obj[1]>2:
								return 'False'
							else: return 'False'
						elif obj[2]<=1:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[11]>0:
					# {"feature": "Coupon", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[4]<=1:
				# {"feature": "Education", "instances": 10, "metric_value": 0.7219, "depth": 4}
				if obj[6]<=2:
					return 'True'
				elif obj[6]>2:
					# {"feature": "Occupation", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[7]<=1:
						return 'True'
					elif obj[7]>1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Education", "instances": 20, "metric_value": 0.6098, "depth": 2}
		if obj[6]>0:
			return 'True'
		elif obj[6]<=0:
			# {"feature": "Distance", "instances": 9, "metric_value": 0.9183, "depth": 3}
			if obj[12]>1:
				# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[8]<=1.0:
					return 'False'
				elif obj[8]>1.0:
					return 'True'
				else: return 'True'
			elif obj[12]<=1:
				return 'True'
			else: return 'True'
		else: return 'True'
	else: return 'True'
