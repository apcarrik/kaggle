def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Bar", "instances": 21, "metric_value": 0.9852, "depth": 2}
		if obj[8]<=2.0:
			# {"feature": "Coupon", "instances": 18, "metric_value": 1.0, "depth": 3}
			if obj[2]>1:
				# {"feature": "Education", "instances": 14, "metric_value": 0.9403, "depth": 4}
				if obj[6]<=2:
					# {"feature": "Occupation", "instances": 12, "metric_value": 0.8113, "depth": 5}
					if obj[7]<=6:
						# {"feature": "Age", "instances": 7, "metric_value": 0.9852, "depth": 6}
						if obj[4]>0:
							# {"feature": "Coffeehouse", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[9]>0.0:
								return 'True'
							elif obj[9]<=0.0:
								# {"feature": "Gender", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[3]<=0:
									return 'False'
								elif obj[3]>0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]<=0:
							return 'False'
						else: return 'False'
					elif obj[7]>6:
						return 'True'
					else: return 'True'
				elif obj[6]>2:
					return 'False'
				else: return 'False'
			elif obj[2]<=1:
				return 'False'
			else: return 'False'
		elif obj[8]>2.0:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.6194, "depth": 2}
		if obj[9]>0.0:
			return 'True'
		elif obj[9]<=0.0:
			# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 3}
			if obj[1]>2:
				# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 4}
				if obj[2]>2:
					# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[4]>0:
						return 'False'
					elif obj[4]<=0:
						return 'True'
					else: return 'True'
				elif obj[2]<=2:
					return 'True'
				else: return 'True'
			elif obj[1]<=2:
				return 'False'
			else: return 'False'
		else: return 'False'
	else: return 'True'
