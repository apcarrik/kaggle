def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Age", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[4]<=3:
		# {"feature": "Occupation", "instances": 18, "metric_value": 0.7642, "depth": 2}
		if obj[6]>4:
			return 'False'
		elif obj[6]<=4:
			# {"feature": "Coupon", "instances": 7, "metric_value": 0.9852, "depth": 3}
			if obj[2]<=3:
				# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[8]<=2.0:
					return 'True'
				elif obj[8]>2.0:
					return 'False'
				else: return 'False'
			elif obj[2]>3:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[4]>3:
		# {"feature": "Occupation", "instances": 16, "metric_value": 0.9887, "depth": 2}
		if obj[6]<=7:
			# {"feature": "Direction_same", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[10]<=0:
				# {"feature": "Coupon", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[2]>2:
					# {"feature": "Passanger", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[0]<=1:
						# {"feature": "Time", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[1]<=3:
							return 'True'
						elif obj[1]>3:
							# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[5]>2:
								return 'True'
							elif obj[5]<=2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[0]>1:
						return 'False'
					else: return 'False'
				elif obj[2]<=2:
					return 'False'
				else: return 'False'
			elif obj[10]>0:
				return 'True'
			else: return 'True'
		elif obj[6]>7:
			return 'True'
		else: return 'True'
	else: return 'True'
