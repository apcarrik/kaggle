def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Passanger", "instances": 51, "metric_value": 0.9526, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Direction_same", "instances": 34, "metric_value": 1.0, "depth": 2}
		if obj[12]<=0:
			# {"feature": "Occupation", "instances": 20, "metric_value": 0.9341, "depth": 3}
			if obj[7]>6:
				# {"feature": "Age", "instances": 14, "metric_value": 0.7496, "depth": 4}
				if obj[4]>2:
					return 'False'
				elif obj[4]<=2:
					# {"feature": "Education", "instances": 5, "metric_value": 0.971, "depth": 5}
					if obj[6]>1:
						return 'True'
					elif obj[6]<=1:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[7]<=6:
				# {"feature": "Time", "instances": 6, "metric_value": 0.9183, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[6]<=2:
						return 'False'
					elif obj[6]>2:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'True'
				else: return 'True'
			else: return 'True'
		elif obj[12]>0:
			# {"feature": "Coffeehouse", "instances": 14, "metric_value": 0.8631, "depth": 3}
			if obj[10]<=3.0:
				# {"feature": "Bar", "instances": 13, "metric_value": 0.7793, "depth": 4}
				if obj[9]<=0.0:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.9544, "depth": 5}
					if obj[2]>1:
						# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[4]<=5:
							# {"feature": "Children", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[5]<=0:
								return 'True'
							elif obj[5]>0:
								# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[1]>0:
									return 'False'
								elif obj[1]<=0:
									return 'True'
								else: return 'True'
							else: return 'False'
						elif obj[4]>5:
							return 'False'
						else: return 'False'
					elif obj[2]<=1:
						return 'True'
					else: return 'True'
				elif obj[9]>0.0:
					return 'True'
				else: return 'True'
			elif obj[10]>3.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Income", "instances": 17, "metric_value": 0.5226, "depth": 2}
		if obj[8]<=5:
			return 'True'
		elif obj[8]>5:
			return 'False'
		else: return 'False'
	else: return 'True'
