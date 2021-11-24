def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Time", "instances": 34, "metric_value": 0.99, "depth": 1}
	if obj[1]<=2:
		# {"feature": "Coupon", "instances": 20, "metric_value": 0.9341, "depth": 2}
		if obj[2]<=3:
			# {"feature": "Occupation", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[5]<=12:
				# {"feature": "Restaurant20to50", "instances": 10, "metric_value": 0.8813, "depth": 4}
				if obj[8]<=1.0:
					# {"feature": "Age", "instances": 6, "metric_value": 1.0, "depth": 5}
					if obj[3]<=3:
						# {"feature": "Coffeehouse", "instances": 4, "metric_value": 0.8113, "depth": 6}
						if obj[7]>0.0:
							return 'True'
						elif obj[7]<=0.0:
							return 'False'
						else: return 'False'
					elif obj[3]>3:
						return 'False'
					else: return 'False'
				elif obj[8]>1.0:
					return 'True'
				else: return 'True'
			elif obj[5]>12:
				return 'False'
			else: return 'False'
		elif obj[2]>3:
			return 'False'
		else: return 'False'
	elif obj[1]>2:
		# {"feature": "Age", "instances": 14, "metric_value": 0.5917, "depth": 2}
		if obj[3]<=6:
			# {"feature": "Direction_same", "instances": 13, "metric_value": 0.3912, "depth": 3}
			if obj[9]<=0:
				return 'True'
			elif obj[9]>0:
				return 'False'
			else: return 'False'
		elif obj[3]>6:
			return 'False'
		else: return 'False'
	else: return 'True'
