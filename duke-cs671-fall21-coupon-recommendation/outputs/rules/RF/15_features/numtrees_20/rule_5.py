def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Distance", "instances": 51, "metric_value": 0.9864, "depth": 1}
	if obj[14]<=2:
		# {"feature": "Occupation", "instances": 41, "metric_value": 0.9996, "depth": 2}
		if obj[8]<=8:
			# {"feature": "Education", "instances": 24, "metric_value": 0.8709, "depth": 3}
			if obj[7]<=2:
				# {"feature": "Bar", "instances": 18, "metric_value": 0.9641, "depth": 4}
				if obj[10]<=2.0:
					# {"feature": "Age", "instances": 14, "metric_value": 1.0, "depth": 5}
					if obj[5]<=2:
						# {"feature": "Restaurant20to50", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[12]<=2.0:
							# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 7}
							if obj[2]>1:
								return 'True'
							elif obj[2]<=1:
								# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[0]<=0:
									return 'True'
								elif obj[0]>0:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[12]>2.0:
							return 'False'
						else: return 'False'
					elif obj[5]>2:
						# {"feature": "Time", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[1]>0:
							return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[10]>2.0:
					return 'True'
				else: return 'True'
			elif obj[7]>2:
				return 'True'
			else: return 'True'
		elif obj[8]>8:
			# {"feature": "Age", "instances": 17, "metric_value": 0.7871, "depth": 3}
			if obj[5]>1:
				# {"feature": "Bar", "instances": 11, "metric_value": 0.4395, "depth": 4}
				if obj[10]<=1.0:
					return 'False'
				elif obj[10]>1.0:
					# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[2]>1:
						return 'False'
					elif obj[2]<=1:
						return 'True'
					else: return 'True'
				else: return 'False'
			elif obj[5]<=1:
				# {"feature": "Time", "instances": 6, "metric_value": 1.0, "depth": 4}
				if obj[1]>2:
					return 'False'
				elif obj[1]<=2:
					return 'True'
				else: return 'True'
			else: return 'False'
		else: return 'False'
	elif obj[14]>2:
		# {"feature": "Coupon", "instances": 10, "metric_value": 0.469, "depth": 2}
		if obj[2]<=2:
			return 'False'
		elif obj[2]>2:
			# {"feature": "Gender", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[4]>0:
				return 'True'
			elif obj[4]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
