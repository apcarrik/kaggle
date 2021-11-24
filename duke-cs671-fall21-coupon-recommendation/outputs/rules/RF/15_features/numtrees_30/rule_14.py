def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Restaurant20to50", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[12]>0.0:
		# {"feature": "Occupation", "instances": 25, "metric_value": 0.9988, "depth": 2}
		if obj[8]<=19:
			# {"feature": "Distance", "instances": 22, "metric_value": 0.976, "depth": 3}
			if obj[14]>1:
				# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.874, "depth": 4}
				if obj[11]>0.0:
					# {"feature": "Coupon", "instances": 13, "metric_value": 0.6194, "depth": 5}
					if obj[2]<=2:
						# {"feature": "Time", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[1]>0:
							# {"feature": "Coupon_validity", "instances": 5, "metric_value": 0.971, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 8}
								if obj[4]>0:
									return 'False'
								elif obj[4]<=0:
									return 'True'
								else: return 'True'
							elif obj[3]>0:
								return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'False'
						else: return 'False'
					elif obj[2]>2:
						return 'False'
					else: return 'False'
				elif obj[11]<=0.0:
					# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[2]>2:
						return 'True'
					elif obj[2]<=2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[14]<=1:
				# {"feature": "Bar", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[10]<=2.0:
					return 'True'
				elif obj[10]>2.0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[8]>19:
			return 'True'
		else: return 'True'
	elif obj[12]<=0.0:
		# {"feature": "Coupon", "instances": 9, "metric_value": 0.5033, "depth": 2}
		if obj[2]>1:
			return 'True'
		elif obj[2]<=1:
			# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 3}
			if obj[1]<=0:
				return 'False'
			elif obj[1]>0:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
