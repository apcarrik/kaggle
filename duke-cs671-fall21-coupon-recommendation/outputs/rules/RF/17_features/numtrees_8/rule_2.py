def findDecision(obj): #obj[0]: Passanger, obj[1]: Weather, obj[2]: Time, obj[3]: Coupon, obj[4]: Coupon_validity, obj[5]: Gender, obj[6]: Age, obj[7]: Maritalstatus, obj[8]: Children, obj[9]: Education, obj[10]: Occupation, obj[11]: Income, obj[12]: Bar, obj[13]: Coffeehouse, obj[14]: Restaurant20to50, obj[15]: Direction_same, obj[16]: Distance
	# {"feature": "Coupon", "instances": 127, "metric_value": 0.9719, "depth": 1}
	if obj[3]>1:
		# {"feature": "Direction_same", "instances": 88, "metric_value": 0.8288, "depth": 2}
		if obj[15]<=0:
			# {"feature": "Coffeehouse", "instances": 69, "metric_value": 0.6981, "depth": 3}
			if obj[13]<=1.0:
				# {"feature": "Coupon_validity", "instances": 37, "metric_value": 0.878, "depth": 4}
				if obj[4]<=0:
					# {"feature": "Age", "instances": 20, "metric_value": 0.6098, "depth": 5}
					if obj[6]>0:
						return 'True'
					elif obj[6]<=0:
						# {"feature": "Time", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[2]>1:
							# {"feature": "Restaurant20to50", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[14]>0.0:
								return 'False'
							elif obj[14]<=0.0:
								return 'True'
							else: return 'True'
						elif obj[2]<=1:
							return 'True'
						else: return 'True'
					else: return 'True'
				elif obj[4]>0:
					# {"feature": "Income", "instances": 17, "metric_value": 0.9975, "depth": 5}
					if obj[11]<=4:
						# {"feature": "Maritalstatus", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[7]<=1:
							return 'True'
						elif obj[7]>1:
							# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[5]>0:
								return 'True'
							elif obj[5]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[11]>4:
						# {"feature": "Time", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[5]>0:
								return 'False'
							elif obj[5]<=0:
								return 'True'
							else: return 'True'
						else: return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[13]>1.0:
				# {"feature": "Bar", "instances": 32, "metric_value": 0.3373, "depth": 4}
				if obj[12]<=1.0:
					return 'True'
				elif obj[12]>1.0:
					# {"feature": "Restaurant20to50", "instances": 12, "metric_value": 0.65, "depth": 5}
					if obj[14]>0.0:
						# {"feature": "Education", "instances": 11, "metric_value": 0.4395, "depth": 6}
						if obj[9]<=2:
							return 'True'
						elif obj[9]>2:
							# {"feature": "Weather", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]>0:
								return 'True'
							elif obj[1]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[14]<=0.0:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		elif obj[15]>0:
			# {"feature": "Education", "instances": 19, "metric_value": 0.998, "depth": 3}
			if obj[9]>0:
				# {"feature": "Maritalstatus", "instances": 11, "metric_value": 0.684, "depth": 4}
				if obj[7]<=1:
					return 'False'
				elif obj[7]>1:
					# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]>0:
						return 'True'
					elif obj[6]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[9]<=0:
				# {"feature": "Age", "instances": 8, "metric_value": 0.5436, "depth": 4}
				if obj[6]<=4:
					return 'True'
				elif obj[6]>4:
					# {"feature": "Maritalstatus", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[7]>1:
						return 'True'
					elif obj[7]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[3]<=1:
		# {"feature": "Occupation", "instances": 39, "metric_value": 0.8582, "depth": 2}
		if obj[10]<=14:
			# {"feature": "Bar", "instances": 31, "metric_value": 0.9383, "depth": 3}
			if obj[12]>0.0:
				# {"feature": "Age", "instances": 16, "metric_value": 0.9887, "depth": 4}
				if obj[6]>0:
					# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.8454, "depth": 5}
					if obj[14]>-1.0:
						# {"feature": "Income", "instances": 10, "metric_value": 0.7219, "depth": 6}
						if obj[11]>2:
							return 'True'
						elif obj[11]<=2:
							# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[0]>0:
								# {"feature": "Maritalstatus", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[7]>0:
									return 'True'
								elif obj[7]<=0:
									return 'False'
								else: return 'False'
							elif obj[0]<=0:
								return 'False'
							else: return 'False'
						else: return 'False'
					elif obj[14]<=-1.0:
						return 'False'
					else: return 'False'
				elif obj[6]<=0:
					# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[0]>0:
						return 'False'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[12]<=0.0:
				# {"feature": "Gender", "instances": 15, "metric_value": 0.5665, "depth": 4}
				if obj[5]>0:
					return 'False'
				elif obj[5]<=0:
					# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[13]<=1.0:
						return 'False'
					elif obj[13]>1.0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[10]>14:
			return 'False'
		else: return 'False'
	else: return 'False'
