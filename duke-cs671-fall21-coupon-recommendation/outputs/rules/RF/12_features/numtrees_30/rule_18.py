def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Education, obj[6]: Occupation, obj[7]: Bar, obj[8]: Coffeehouse, obj[9]: Restaurant20to50, obj[10]: Direction_same, obj[11]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9774, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Restaurant20to50", "instances": 22, "metric_value": 0.994, "depth": 2}
		if obj[9]<=1.0:
			# {"feature": "Direction_same", "instances": 12, "metric_value": 0.8113, "depth": 3}
			if obj[10]<=0:
				# {"feature": "Education", "instances": 10, "metric_value": 0.469, "depth": 4}
				if obj[5]<=3:
					return 'False'
				elif obj[5]>3:
					return 'True'
				else: return 'True'
			elif obj[10]>0:
				return 'True'
			else: return 'True'
		elif obj[9]>1.0:
			# {"feature": "Age", "instances": 10, "metric_value": 0.8813, "depth": 3}
			if obj[4]<=4:
				# {"feature": "Coffeehouse", "instances": 9, "metric_value": 0.7642, "depth": 4}
				if obj[8]>0.0:
					# {"feature": "Coupon", "instances": 8, "metric_value": 0.5436, "depth": 5}
					if obj[2]>0:
						return 'True'
					elif obj[2]<=0:
						# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[1]>0:
							return 'False'
						elif obj[1]<=0:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[8]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[4]>4:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>2:
		# {"feature": "Coffeehouse", "instances": 12, "metric_value": 0.65, "depth": 2}
		if obj[8]>0.0:
			return 'True'
		elif obj[8]<=0.0:
			return 'False'
		else: return 'False'
	else: return 'True'
