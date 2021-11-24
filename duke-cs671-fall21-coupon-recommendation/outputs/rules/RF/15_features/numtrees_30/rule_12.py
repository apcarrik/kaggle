def findDecision(obj): #obj[0]: Passanger, obj[1]: Time, obj[2]: Coupon, obj[3]: Coupon_validity, obj[4]: Gender, obj[5]: Age, obj[6]: Children, obj[7]: Education, obj[8]: Occupation, obj[9]: Income, obj[10]: Bar, obj[11]: Coffeehouse, obj[12]: Restaurant20to50, obj[13]: Direction_same, obj[14]: Distance
	# {"feature": "Coffeehouse", "instances": 34, "metric_value": 0.9367, "depth": 1}
	if obj[11]>0.0:
		# {"feature": "Coupon", "instances": 27, "metric_value": 0.7642, "depth": 2}
		if obj[2]<=2:
			# {"feature": "Education", "instances": 16, "metric_value": 0.9544, "depth": 3}
			if obj[7]<=2:
				# {"feature": "Occupation", "instances": 12, "metric_value": 0.8113, "depth": 4}
				if obj[8]<=22:
					# {"feature": "Restaurant20to50", "instances": 11, "metric_value": 0.684, "depth": 5}
					if obj[12]>0.0:
						# {"feature": "Distance", "instances": 10, "metric_value": 0.469, "depth": 6}
						if obj[14]<=2:
							return 'True'
						elif obj[14]>2:
							# {"feature": "Coupon_validity", "instances": 2, "metric_value": 1.0, "depth": 7}
							if obj[3]>0:
								return 'True'
							elif obj[3]<=0:
								return 'False'
							else: return 'False'
						else: return 'True'
					elif obj[12]<=0.0:
						return 'False'
					else: return 'False'
				elif obj[8]>22:
					return 'False'
				else: return 'False'
			elif obj[7]>2:
				# {"feature": "Occupation", "instances": 4, "metric_value": 0.8113, "depth": 4}
				if obj[8]>4:
					return 'False'
				elif obj[8]<=4:
					return 'True'
				else: return 'True'
			else: return 'False'
		elif obj[2]>2:
			return 'True'
		else: return 'True'
	elif obj[11]<=0.0:
		# {"feature": "Education", "instances": 7, "metric_value": 0.5917, "depth": 2}
		if obj[7]<=2:
			return 'False'
		elif obj[7]>2:
			return 'True'
		else: return 'True'
	else: return 'False'
