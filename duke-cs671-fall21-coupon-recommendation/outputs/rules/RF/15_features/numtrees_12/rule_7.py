def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coffeehouse", "instances": 85, "metric_value": 0.9879, "depth": 1}
	if obj[11]>0.0:
		# {"feature": "Time", "instances": 56, "metric_value": 0.8856, "depth": 2}
		if obj[1]>0:
			# {"feature": "Coupon", "instances": 42, "metric_value": 0.7025, "depth": 3}
			if obj[2]>1:
				# {"feature": "Restaurant20to50", "instances": 27, "metric_value": 0.3809, "depth": 4}
				if obj[12]<=1.0:
					return 'True'
				elif obj[12]>1.0:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[0]>1:
						return 'True'
					elif obj[0]<=1:
						# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]>0:
							return 'False'
						elif obj[6]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				else: return 'True'
			elif obj[2]<=1:
				# {"feature": "Age", "instances": 15, "metric_value": 0.971, "depth": 4}
				if obj[5]>1:
					# {"feature": "Bar", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[10]<=2.0:
						# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[12]<=2.0:
							# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[7]<=0:
								return 'False'
							elif obj[7]>0:
								# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[8]>7:
									return 'True'
								elif obj[8]<=7:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[12]>2.0:
							return 'True'
						else: return 'True'
					elif obj[10]>2.0:
						return 'True'
					else: return 'True'
				elif obj[5]<=1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[1]<=0:
			# {"feature": "Gender", "instances": 14, "metric_value": 0.9403, "depth": 3}
			if obj[4]<=0:
				# {"feature": "Passanger", "instances": 8, "metric_value": 0.9544, "depth": 4}
				if obj[0]<=1:
					return 'True'
				elif obj[0]>1:
					# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[8]>1:
						return 'False'
					elif obj[8]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[4]>0:
				return 'False'
			else: return 'False'
		else: return 'False'
	elif obj[11]<=0.0:
		# {"feature": "Education", "instances": 29, "metric_value": 0.8936, "depth": 2}
		if obj[7]<=2:
			# {"feature": "Income", "instances": 22, "metric_value": 0.976, "depth": 3}
			if obj[9]<=7:
				# {"feature": "Time", "instances": 20, "metric_value": 0.9341, "depth": 4}
				if obj[1]<=3:
					# {"feature": "Age", "instances": 17, "metric_value": 0.9774, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Coupon", "instances": 13, "metric_value": 0.8905, "depth": 6}
						if obj[2]>1:
							# {"feature": "Passanger", "instances": 8, "metric_value": 1.0, "depth": 7}
							if obj[0]<=1:
								# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.7219, "depth": 8}
								if obj[3]>0:
									return 'False'
								elif obj[3]<=0:
									return 'True'
								else: return 'True'
							elif obj[0]>1:
								return 'True'
							else: return 'True'
						elif obj[2]<=1:
							return 'False'
						else: return 'False'
					elif obj[5]>2:
						# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[4]<=0:
							return 'True'
						elif obj[4]>0:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]>3:
					return 'False'
				else: return 'False'
			elif obj[9]>7:
				return 'True'
			else: return 'True'
		elif obj[7]>2:
			return 'False'
		else: return 'False'
	else: return 'False'
