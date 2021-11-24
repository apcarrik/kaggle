def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Age", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[4]>1:
		# {"feature": "Coffeehouse", "instances": 34, "metric_value": 1.0, "depth": 2}
		if obj[8]>0.0:
			# {"feature": "Coupon", "instances": 23, "metric_value": 0.9321, "depth": 3}
			if obj[2]<=2:
				# {"feature": "Education", "instances": 14, "metric_value": 0.9852, "depth": 4}
				if obj[5]<=2:
					# {"feature": "Occupation", "instances": 12, "metric_value": 0.9183, "depth": 5}
					if obj[6]<=9:
						# {"feature": "Time", "instances": 8, "metric_value": 1.0, "depth": 6}
						if obj[1]>0:
							# {"feature": "Gender", "instances": 6, "metric_value": 0.9183, "depth": 7}
							if obj[3]<=0:
								return 'False'
							elif obj[3]>0:
								# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 8}
								if obj[0]>1:
									# {"feature": "Bar", "instances": 2, "metric_value": 1.0, "depth": 9}
									if obj[7]<=0.0:
										return 'True'
									elif obj[7]>0.0:
										return 'False'
									else: return 'False'
								elif obj[0]<=1:
									return 'True'
								else: return 'True'
							else: return 'True'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					elif obj[6]>9:
						return 'False'
					else: return 'False'
				elif obj[5]>2:
					return 'True'
				else: return 'True'
			elif obj[2]>2:
				return 'True'
			else: return 'True'
		elif obj[8]<=0.0:
			# {"feature": "Education", "instances": 11, "metric_value": 0.684, "depth": 3}
			if obj[5]<=3:
				# {"feature": "Time", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[1]>0:
					return 'False'
				elif obj[1]<=0:
					# {"feature": "Passanger", "instances": 2, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						return 'True'
					elif obj[0]<=0:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]>3:
				return 'True'
			else: return 'True'
		else: return 'False'
	elif obj[4]<=1:
		# {"feature": "Coffeehouse", "instances": 17, "metric_value": 0.5226, "depth": 2}
		if obj[8]<=2.0:
			return 'True'
		elif obj[8]>2.0:
			# {"feature": "Occupation", "instances": 3, "metric_value": 0.9183, "depth": 3}
			if obj[6]<=1:
				return 'False'
			elif obj[6]>1:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'True'
