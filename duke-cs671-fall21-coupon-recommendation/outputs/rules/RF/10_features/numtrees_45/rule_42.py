def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Education", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[3]<=2:
		# {"feature": "Passanger", "instances": 18, "metric_value": 0.9911, "depth": 2}
		if obj[0]<=1:
			# {"feature": "Bar", "instances": 12, "metric_value": 0.9799, "depth": 3}
			if obj[5]>0.0:
				# {"feature": "Coupon", "instances": 8, "metric_value": 0.8113, "depth": 4}
				if obj[2]<=2:
					# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 5}
					if obj[1]>0:
						# {"feature": "Coffeehouse", "instances": 3, "metric_value": 0.9183, "depth": 6}
						if obj[6]<=1.0:
							return 'True'
						elif obj[6]>1.0:
							return 'False'
						else: return 'False'
					elif obj[1]<=0:
						return 'False'
					else: return 'False'
				elif obj[2]>2:
					return 'False'
				else: return 'False'
			elif obj[5]<=0.0:
				# {"feature": "Coupon", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[2]>0:
					return 'True'
				elif obj[2]<=0:
					return 'False'
				else: return 'False'
			else: return 'True'
		elif obj[0]>1:
			# {"feature": "Restaurant20to50", "instances": 6, "metric_value": 0.65, "depth": 3}
			if obj[7]>0.0:
				return 'True'
			elif obj[7]<=0.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[3]>2:
		return 'True'
	else: return 'True'
