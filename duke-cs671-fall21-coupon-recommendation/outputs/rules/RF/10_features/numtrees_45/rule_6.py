def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Passanger", "instances": 23, "metric_value": 0.9321, "depth": 1}
	if obj[0]<=1:
		# {"feature": "Coupon", "instances": 14, "metric_value": 0.9852, "depth": 2}
		if obj[2]<=0:
			# {"feature": "Bar", "instances": 8, "metric_value": 0.8113, "depth": 3}
			if obj[5]>0.0:
				# {"feature": "Time", "instances": 4, "metric_value": 1.0, "depth": 4}
				if obj[1]<=1:
					# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 5}
					if obj[3]<=0:
						# {"feature": "Occupation", "instances": 2, "metric_value": 1.0, "depth": 6}
						if obj[4]<=21:
							return 'False'
						elif obj[4]>21:
							return 'True'
						else: return 'True'
					elif obj[3]>0:
						return 'True'
					else: return 'True'
				elif obj[1]>1:
					return 'False'
				else: return 'False'
			elif obj[5]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[2]>0:
			# {"feature": "Bar", "instances": 6, "metric_value": 0.9183, "depth": 3}
			if obj[5]<=2.0:
				# {"feature": "Coffeehouse", "instances": 5, "metric_value": 0.7219, "depth": 4}
				if obj[6]>0.0:
					return 'True'
				elif obj[6]<=0.0:
					return 'False'
				else: return 'False'
			elif obj[5]>2.0:
				return 'False'
			else: return 'False'
		else: return 'True'
	elif obj[0]>1:
		return 'True'
	else: return 'True'
