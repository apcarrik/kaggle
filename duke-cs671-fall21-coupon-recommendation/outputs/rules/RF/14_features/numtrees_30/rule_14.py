def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Income, obj[9]: Bar, obj[10]: Coffeehouse, obj[11]: Restaurant20to50, obj[12]: Direction_same, obj[13]: Distance
	# {"feature": "Income", "instances": 34, "metric_value": 0.9597, "depth": 1}
	if obj[8]>0:
		# {"feature": "Passanger", "instances": 31, "metric_value": 0.9072, "depth": 2}
		if obj[0]>0:
			# {"feature": "Coupon", "instances": 27, "metric_value": 0.8256, "depth": 3}
			if obj[2]>0:
				# {"feature": "Time", "instances": 19, "metric_value": 0.9495, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Children", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[5]>0:
						# {"feature": "Occupation", "instances": 6, "metric_value": 0.9183, "depth": 6}
						if obj[7]>1:
							return 'False'
						elif obj[7]<=1:
							# {"feature": "Age", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[4]>1:
								return 'True'
							elif obj[4]<=1:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[5]<=0:
						# {"feature": "Age", "instances": 6, "metric_value": 0.65, "depth": 6}
						if obj[4]<=4:
							return 'True'
						elif obj[4]>4:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			elif obj[2]<=0:
				return 'False'
			else: return 'False'
		elif obj[0]<=0:
			# {"feature": "Gender", "instances": 4, "metric_value": 0.8113, "depth": 3}
			if obj[3]>0:
				return 'True'
			elif obj[3]<=0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[8]<=0:
		return 'True'
	else: return 'True'
