def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Direction_same", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[10]<=0:
		# {"feature": "Coupon", "instances": 29, "metric_value": 0.9923, "depth": 2}
		if obj[2]>1:
			# {"feature": "Restaurant20to50", "instances": 26, "metric_value": 0.9612, "depth": 3}
			if obj[9]>0.0:
				# {"feature": "Age", "instances": 18, "metric_value": 0.7642, "depth": 4}
				if obj[4]<=2:
					# {"feature": "Time", "instances": 10, "metric_value": 0.971, "depth": 5}
					if obj[1]>1:
						# {"feature": "Occupation", "instances": 8, "metric_value": 0.8113, "depth": 6}
						if obj[6]<=11:
							return 'True'
						elif obj[6]>11:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]>1:
								return 'False'
							elif obj[0]<=1:
								return 'True'
							else: return 'True'
						else: return 'False'
					elif obj[1]<=1:
						return 'False'
					else: return 'False'
				elif obj[4]>2:
					return 'True'
				else: return 'True'
			elif obj[9]<=0.0:
				# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[4]>0:
					# {"feature": "Passanger", "instances": 7, "metric_value": 0.5917, "depth": 5}
					if obj[0]<=1:
						return 'False'
					elif obj[0]>1:
						# {"feature": "Time", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[1]>3:
							return 'False'
						elif obj[1]<=3:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[4]<=0:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]<=1:
			return 'False'
		else: return 'False'
	elif obj[10]>0:
		return 'True'
	else: return 'True'
