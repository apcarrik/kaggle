def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Gender, obj[4]: Age, obj[5]: Children, obj[6]: Education, obj[7]: Occupation, obj[8]: Bar, obj[9]: Coffeehouse, obj[10]: Restaurant20to50, obj[11]: Direction_same, obj[12]: Distance
	# {"feature": "Restaurant20to50", "instances": 23, "metric_value": 0.9877, "depth": 1}
	if obj[10]<=1.0:
		# {"feature": "Time", "instances": 16, "metric_value": 0.9887, "depth": 2}
		if obj[1]>0:
			# {"feature": "Coffeehouse", "instances": 13, "metric_value": 0.9957, "depth": 3}
			if obj[9]<=1.0:
				# {"feature": "Passanger", "instances": 10, "metric_value": 0.971, "depth": 4}
				if obj[0]<=2:
					# {"feature": "Age", "instances": 8, "metric_value": 0.8113, "depth": 5}
					if obj[4]>1:
						# {"feature": "Coupon", "instances": 5, "metric_value": 0.971, "depth": 6}
						if obj[2]>0:
							# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 7}
							if obj[7]>1:
								return 'False'
							elif obj[7]<=1:
								return 'True'
							else: return 'True'
						elif obj[2]<=0:
							return 'True'
						else: return 'True'
					elif obj[4]<=1:
						return 'False'
					else: return 'False'
				elif obj[0]>2:
					return 'True'
				else: return 'True'
			elif obj[9]>1.0:
				return 'True'
			else: return 'True'
		elif obj[1]<=0:
			return 'False'
		else: return 'False'
	elif obj[10]>1.0:
		# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[6]<=2:
			return 'True'
		elif obj[6]>2:
			return 'False'
		else: return 'False'
	else: return 'True'
