def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Children, obj[8]: Education, obj[9]: Occupation, obj[10]: Income, obj[11]: Bar, obj[12]: Coffeehouse, obj[13]: Restaurant20to50, obj[14]: Direction_same, obj[15]: Distance
	# {"feature": "Restaurant20to50", "instances": 85, "metric_value": 0.9991, "depth": 1}
	if obj[13]<=1.0:
		# {"feature": "Passanger", "instances": 60, "metric_value": 0.9799, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Direction_same", "instances": 45, "metric_value": 0.9183, "depth": 3}
			if obj[14]<=0:
				# {"feature": "Coupon", "instances": 33, "metric_value": 0.799, "depth": 4}
				if obj[3]>1:
					# {"feature": "Children", "instances": 22, "metric_value": 0.9457, "depth": 5}
					if obj[7]>0:
						# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 6}
						if obj[9]>7:
							# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[6]<=6:
								return 'False'
							elif obj[6]>6:
								return 'True'
							else: return 'True'
						elif obj[9]<=7:
							return 'True'
						else: return 'True'
					elif obj[7]<=0:
						# {"feature": "Time", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[3]<=1:
					return 'False'
				else: return 'False'
			elif obj[14]>0:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.9799, "depth": 4}
				if obj[9]<=6:
					# {"feature": "Children", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[7]<=0:
						# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[2]>0:
							# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[15]<=1:
								# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]>1:
									return 'False'
								elif obj[3]<=1:
									return 'True'
								else: return 'True'
							elif obj[15]>1:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'False'
						else: return 'False'
					elif obj[7]>0:
						return 'False'
					else: return 'False'
				elif obj[9]>6:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[0]>2:
			# {"feature": "Coupon_validity", "instances": 15, "metric_value": 0.9183, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Income", "instances": 9, "metric_value": 0.5033, "depth": 4}
				if obj[10]<=6:
					return 'True'
				elif obj[10]>6:
					return 'False'
				else: return 'False'
			elif obj[4]>0:
				# {"feature": "Age", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[6]<=4:
					# {"feature": "Occupation", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[9]<=12:
						return 'False'
					elif obj[9]>12:
						return 'True'
					else: return 'True'
				elif obj[6]>4:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'True'
	elif obj[13]>1.0:
		# {"feature": "Time", "instances": 25, "metric_value": 0.795, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Occupation", "instances": 14, "metric_value": 0.9852, "depth": 3}
			if obj[9]<=7:
				# {"feature": "Children", "instances": 9, "metric_value": 0.9183, "depth": 4}
				if obj[7]<=0:
					# {"feature": "Distance", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[15]<=1:
						# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[0]>0:
							return 'False'
						elif obj[0]<=0:
							return 'True'
						else: return 'True'
					elif obj[15]>1:
						return 'True'
					else: return 'True'
				elif obj[7]>0:
					return 'False'
				else: return 'False'
			elif obj[9]>7:
				return 'True'
			else: return 'True'
		elif obj[2]>2:
			return 'True'
		else: return 'True'
	else: return 'True'
