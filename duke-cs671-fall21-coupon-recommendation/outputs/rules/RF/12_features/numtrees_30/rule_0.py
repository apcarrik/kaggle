def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Coupon", "instances": 34, "metric_value": 1.0, "depth": 1}
	if obj[2]>2:
		# {"feature": "Passanger", "instances": 20, "metric_value": 0.8813, "depth": 2}
		if obj[0]<=2:
			# {"feature": "Age", "instances": 15, "metric_value": 0.971, "depth": 3}
			if obj[4]<=4:
				# {"feature": "Distance", "instances": 12, "metric_value": 1.0, "depth": 4}
				if obj[11]<=2:
					# {"feature": "Gender", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[3]>0:
						# {"feature": "Coffeehouse", "instances": 6, "metric_value": 1.0, "depth": 6}
						if obj[8]>0.0:
							# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[6]>4:
								return 'True'
							elif obj[6]<=4:
								return 'False'
							else: return 'False'
						elif obj[8]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[3]<=0:
						return 'False'
					else: return 'False'
				elif obj[11]>2:
					return 'True'
				else: return 'True'
			elif obj[4]>4:
				return 'True'
			else: return 'True'
		elif obj[0]>2:
			return 'True'
		else: return 'True'
	elif obj[2]<=2:
		# {"feature": "Age", "instances": 14, "metric_value": 0.7496, "depth": 2}
		if obj[4]<=5:
			return 'False'
		elif obj[4]>5:
			# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 3}
			if obj[0]<=2:
				# {"feature": "Bar", "instances": 5, "metric_value": 0.971, "depth": 4}
				if obj[7]>-1.0:
					# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=0:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>1:
							return 'False'
						elif obj[1]<=1:
							return 'True'
						else: return 'True'
					elif obj[3]>0:
						return 'False'
					else: return 'False'
				elif obj[7]<=-1.0:
					return 'True'
				else: return 'True'
			elif obj[0]>2:
				return 'True'
			else: return 'True'
		else: return 'False'
	else: return 'False'
