def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Coffeehouse", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[9]<=2.0:
		# {"feature": "Time", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[1]<=3:
			# {"feature": "Occupation", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[7]<=7:
				# {"feature": "Bar", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[8]<=1.0:
					# {"feature": "Age", "instances": 9, "metric_value": 0.9183, "depth": 5}
					if obj[4]<=1:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[2]>3:
							# {"feature": "Passanger", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[0]<=2:
								return 'True'
							elif obj[0]>2:
								return 'False'
							else: return 'False'
						elif obj[2]<=3:
							return 'False'
						else: return 'False'
					elif obj[4]>1:
						return 'True'
					else: return 'True'
				elif obj[8]>1.0:
					return 'False'
				else: return 'False'
			elif obj[7]>7:
				return 'False'
			else: return 'False'
		elif obj[1]>3:
			return 'True'
		else: return 'True'
	elif obj[9]>2.0:
		return 'True'
	else: return 'True'
