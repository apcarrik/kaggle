def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Occupation", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[6]>2:
		# {"feature": "Distance", "instances": 28, "metric_value": 0.9963, "depth": 2}
		if obj[11]<=2:
			# {"feature": "Time", "instances": 25, "metric_value": 0.971, "depth": 3}
			if obj[1]<=3:
				# {"feature": "Gender", "instances": 17, "metric_value": 0.7871, "depth": 4}
				if obj[3]<=0:
					# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.9911, "depth": 5}
					if obj[8]<=2.0:
						# {"feature": "Coupon", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[2]>0:
							# {"feature": "Restaurant20to50", "instances": 5, "metric_value": 0.7219, "depth": 7}
							if obj[9]<=1.0:
								return 'False'
							elif obj[9]>1.0:
								# {"feature": "Age", "instances": 2, "metric_value": 1.0, "depth": 8}
								if obj[4]>2:
									return 'True'
								elif obj[4]<=2:
									return 'False'
								else: return 'False'
							else: return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[8]>2.0:
						return 'True'
					else: return 'True'
				elif obj[3]>0:
					return 'True'
				else: return 'True'
			elif obj[1]>3:
				# {"feature": "Education", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[5]>0:
					return 'False'
				elif obj[5]<=0:
					# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[0]>0:
						# {"feature": "Coupon", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[2]<=2:
							return 'False'
						elif obj[2]>2:
							return 'True'
						else: return 'True'
					elif obj[0]<=0:
						return 'True'
					else: return 'True'
				else: return 'False'
			else: return 'False'
		elif obj[11]>2:
			return 'False'
		else: return 'False'
	elif obj[6]<=2:
		return 'True'
	else: return 'True'
