def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Age, obj[4]: Education, obj[5]: Occupation, obj[6]: Bar, obj[7]: Coffeehouse, obj[8]: Restaurant20to50, obj[9]: Direction_same, obj[10]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.8865, "depth": 1}
	if obj[5]<=7:
		# {"feature": "Restaurant20to50", "instances": 19, "metric_value": 0.9495, "depth": 2}
		if obj[8]>0.0:
			# {"feature": "Education", "instances": 16, "metric_value": 0.9887, "depth": 3}
			if obj[4]<=3:
				# {"feature": "Distance", "instances": 14, "metric_value": 1.0, "depth": 4}
				if obj[10]<=2:
					# {"feature": "Bar", "instances": 12, "metric_value": 0.9799, "depth": 5}
					if obj[6]>0.0:
						# {"feature": "Coupon", "instances": 7, "metric_value": 0.5917, "depth": 6}
						if obj[2]>0:
							return 'False'
						elif obj[2]<=0:
							# {"feature": "Time", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[1]<=2:
								return 'True'
							elif obj[1]>2:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[6]<=0.0:
						# {"feature": "Age", "instances": 5, "metric_value": 0.7219, "depth": 6}
						if obj[3]>1:
							return 'True'
						elif obj[3]<=1:
							return 'False'
						else: return 'False'
					else: return 'True'
				elif obj[10]>2:
					return 'True'
				else: return 'True'
			elif obj[4]>3:
				return 'True'
			else: return 'True'
		elif obj[8]<=0.0:
			return 'True'
		else: return 'True'
	elif obj[5]>7:
		return 'True'
	else: return 'True'
