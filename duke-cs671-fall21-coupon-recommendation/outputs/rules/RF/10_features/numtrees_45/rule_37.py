def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Education, obj[4]: Occupation, obj[5]: Bar, obj[6]: Coffeehouse, obj[7]: Restaurant20to50, obj[8]: Direction_same, obj[9]: Distance
	# {"feature": "Occupation", "instances": 23, "metric_value": 0.9986, "depth": 1}
	if obj[4]<=16:
		# {"feature": "Coffeehouse", "instances": 20, "metric_value": 0.971, "depth": 2}
		if obj[6]>0.0:
			# {"feature": "Bar", "instances": 17, "metric_value": 0.874, "depth": 3}
			if obj[5]>0.0:
				# {"feature": "Distance", "instances": 11, "metric_value": 0.994, "depth": 4}
				if obj[9]>1:
					# {"feature": "Restaurant20to50", "instances": 7, "metric_value": 0.8631, "depth": 5}
					if obj[7]>1.0:
						# {"feature": "Passanger", "instances": 4, "metric_value": 1.0, "depth": 6}
						if obj[0]<=1:
							# {"feature": "Education", "instances": 3, "metric_value": 0.9183, "depth": 7}
							if obj[3]<=3:
								return 'True'
							elif obj[3]>3:
								return 'False'
							else: return 'False'
						elif obj[0]>1:
							return 'False'
						else: return 'False'
					elif obj[7]<=1.0:
						return 'False'
					else: return 'False'
				elif obj[9]<=1:
					# {"feature": "Education", "instances": 4, "metric_value": 0.8113, "depth": 5}
					if obj[3]<=2:
						return 'True'
					elif obj[3]>2:
						return 'False'
					else: return 'False'
				else: return 'True'
			elif obj[5]<=0.0:
				return 'False'
			else: return 'False'
		elif obj[6]<=0.0:
			return 'True'
		else: return 'True'
	elif obj[4]>16:
		return 'True'
	else: return 'True'
