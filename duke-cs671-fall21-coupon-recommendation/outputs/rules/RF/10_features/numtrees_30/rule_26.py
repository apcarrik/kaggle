def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Passanger", "instances": 34, "metric_value": 0.9082, "depth": 1}
	if obj[0]<=2:
		# {"feature": "Coffeehouse", "instances": 26, "metric_value": 0.9829, "depth": 2}
		if obj[6]>0.0:
			# {"feature": "Bar", "instances": 21, "metric_value": 0.9984, "depth": 3}
			if obj[5]<=1.0:
				# {"feature": "Coupon", "instances": 16, "metric_value": 0.9544, "depth": 4}
				if obj[2]<=3:
					# {"feature": "Time", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[1]<=1:
						return 'True'
					elif obj[1]>1:
						# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[3]>1:
							return 'False'
						elif obj[3]<=1:
							return 'True'
						else: return 'True'
					else: return 'False'
				elif obj[2]>3:
					# {"feature": "Time", "instances": 5, "metric_value": 0.7219, "depth": 5}
					if obj[1]>0:
						return 'False'
					elif obj[1]<=0:
						# {"feature": "Education", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[3]<=3:
							return 'True'
						elif obj[3]>3:
							return 'False'
						else: return 'False'
					else: return 'True'
				else: return 'False'
			elif obj[5]>1.0:
				return 'False'
			else: return 'False'
		elif obj[6]<=0.0:
			return 'True'
		else: return 'True'
	elif obj[0]>2:
		return 'True'
	else: return 'True'
