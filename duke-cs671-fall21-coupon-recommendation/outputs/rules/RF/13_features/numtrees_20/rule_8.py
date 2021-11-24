def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Bar", "instances": 51, "metric_value": 0.9774, "depth": 1}
	if obj[8]>0.0:
		# {"feature": "Occupation", "instances": 32, "metric_value": 0.8571, "depth": 2}
		if obj[7]<=12:
			# {"feature": "Time", "instances": 27, "metric_value": 0.6913, "depth": 3}
			if obj[1]>1:
				return 'True'
			elif obj[1]<=1:
				# {"feature": "Coupon", "instances": 13, "metric_value": 0.9612, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Education", "instances": 10, "metric_value": 1.0, "depth": 5}
					if obj[6]<=2:
						# {"feature": "Age", "instances": 7, "metric_value": 0.8631, "depth": 6}
						if obj[4]<=1:
							# {"feature": "Gender", "instances": 4, "metric_value": 1.0, "depth": 7}
							if obj[3]<=0:
								# {"feature": "Children", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[5]<=0:
									return 'False'
								elif obj[5]>0:
									return 'True'
								else: return 'True'
							elif obj[3]>0:
								return 'True'
							else: return 'True'
						elif obj[4]>1:
							return 'False'
						else: return 'False'
					elif obj[6]>2:
						return 'True'
					else: return 'True'
				elif obj[2]>2:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[7]>12:
			# {"feature": "Passanger", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[0]<=1:
				return 'False'
			elif obj[0]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[8]<=0.0:
		# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[10]>0.0:
			# {"feature": "Passanger", "instances": 14, "metric_value": 0.7496, "depth": 3}
			if obj[0]<=2:
				return 'False'
			elif obj[0]>2:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[10]<=0.0:
			# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 3}
			if obj[9]>-1.0:
				return 'True'
			elif obj[9]<=-1.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	else: return 'False'
