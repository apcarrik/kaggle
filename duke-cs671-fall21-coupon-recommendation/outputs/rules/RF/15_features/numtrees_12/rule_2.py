def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coupon_validity", "instances": 85, "metric_value": 0.9999, "depth": 1}
	if obj[3]<=0:
		# {"feature": "Coupon", "instances": 43, "metric_value": 0.9523, "depth": 2}
		if obj[2]>1:
			# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.7554, "depth": 3}
			if obj[12]<=1.0:
				# {"feature": "Time", "instances": 14, "metric_value": 0.9403, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Education", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[7]<=2:
						# {"feature": "Passanger", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[0]>0:
							return 'True'
						elif obj[0]<=0:
							return 'False'
						else: return 'False'
					elif obj[7]>2:
						return 'False'
					else: return 'False'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[12]>1.0:
				return 'True'
			else: return 'True'
		elif obj[2]<=1:
			# {"feature": "Occupation", "instances": 20, "metric_value": 0.9928, "depth": 3}
			if obj[8]<=9:
				# {"feature": "Education", "instances": 15, "metric_value": 0.9183, "depth": 4}
				if obj[7]>1:
					# {"feature": "Time", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[1]<=1:
						# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Gender", "instances": 7, "metric_value": 0.8631, "depth": 7}
							if obj[4]<=0:
								return 'False'
							elif obj[4]>0:
								# {"feature": "Restaurant20to50", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[12]>0.0:
									return 'True'
								elif obj[12]<=0.0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[0]>1:
							return 'True'
						else: return 'True'
					elif obj[1]>1:
						return 'True'
					else: return 'True'
				elif obj[7]<=1:
					return 'False'
				else: return 'False'
			elif obj[8]>9:
				# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[0]>0:
					return 'True'
				elif obj[0]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		else: return 'False'
	elif obj[3]>0:
		# {"feature": "Income", "instances": 42, "metric_value": 0.9587, "depth": 2}
		if obj[9]<=6:
			# {"feature": "Passanger", "instances": 34, "metric_value": 0.874, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Coupon", "instances": 24, "metric_value": 0.65, "depth": 4}
				if obj[2]>2:
					# {"feature": "Occupation", "instances": 15, "metric_value": 0.8366, "depth": 5}
					if obj[8]>5:
						# {"feature": "Age", "instances": 9, "metric_value": 0.5033, "depth": 6}
						if obj[5]<=4:
							return 'False'
						elif obj[5]>4:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=0:
								return 'True'
							elif obj[1]>0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[8]<=5:
						# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[1]<=1:
							# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[10]>0.0:
								# {"feature": "Direction_same", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[13]>0:
									return 'True'
								elif obj[13]<=0:
									return 'False'
								else: return 'False'
							elif obj[10]<=0.0:
								return 'False'
							else: return 'False'
						elif obj[1]>1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]<=2:
					return 'False'
				else: return 'False'
			elif obj[0]>2:
				# {"feature": "Gender", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[4]<=0:
					# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[5]>2:
						return 'True'
					elif obj[5]<=2:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[7]>0:
							return 'False'
						elif obj[7]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[4]>0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[9]>6:
			# {"feature": "Coffeehouse", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[11]>0.0:
				# {"feature": "Age", "instances": 7, "metric_value": 0.5917, "depth": 4}
				if obj[5]>0:
					return 'True'
				elif obj[5]<=0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[11]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
